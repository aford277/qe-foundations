import tempfile
import unittest
from pathlib import Path

from qe_foundations.ingestion import (
    MissingColumnsError,
    SourceNotFoundError,
    load_test_cases,
)

HEADER = "id,title,status,duration\n"


class TestLoadTestCases(unittest.TestCase):

    def setUp(self):
        # A fresh temporary folder for EACH test. addCleanup deletes it
        # even if the test fails, so tests stay independent.
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.folder = Path(temp.name)

    def write_file(self, name, text):
        """Write `text` to a file called `name` in this test's temp folder
        and return its Path."""
        path = self.folder / name
        path.write_text(text, encoding="utf-8")
        return path

    # ---- 1. Happy path -----------------------------------------------------
    def test_good_file_loads_all_rows(self):
        # Arrange
        path = self.write_file(
            "good.csv",
            HEADER
            + "TC-1,Login works,pass,1.5\n"
            + "TC-2,Search works,fail,2\n"
            + "TC-3,Adding works,pass,1\n"
        )

        # Act
        report = load_test_cases(path)

        # Assert
        self.assertEqual(report.rows_seen, 3)
        self.assertEqual(len(report.valid), 3)
        self.assertEqual(len(report.rejected), 0)

    # ---- 2. Bad row is reported, good rows are kept (+ assertLogs) --------
    def test_bad_row_is_rejected_and_good_rows_kept(self):
        # Arrange: one good row, then one bad row
        path = self.write_file(
            "one_bad.csv",
            HEADER
            + "TC-1,Login works,pass,1.5\n"
            + "TC-2,Search works,pass,-3\n"
        )

        # Act: capture the WARNING the loader logs for the bad row
        with self.assertLogs("qe_foundations.ingestion.loader", level="WARNING") as captured:
            report = load_test_cases(path)

        # Assert
        self.assertEqual(len(report.valid), 1)
        self.assertEqual(len(report.rejected), 1)
        self.assertEqual(report.rejected[0].row, 2)
        self.assertIn("Row 2", captured.output[0])

    # ---- 3. Missing file raises -------------------------------------------
    def test_missing_file_raises_source_not_found(self):
        # Arrange: a path in the temp folder that we never create
        path = self.folder / "does_not_exist.csv"

        # Act + Assert
        with self.assertRaises(SourceNotFoundError):
            load_test_cases(path)

    # ---- 4. Missing column raises -----------------------------------------
    def test_missing_column_raises_missing_columns_error(self):
        # Arrange: a CSV whose header has no "duration" column
        path = self.write_file(
            "no_duration.csv",
            "id,title,status\n"
            + "TC-1,Login works,pass\n",
        )

        # Act + Assert
        with self.assertRaises(MissingColumnsError) as ctx:
            load_test_cases(path)
        # TODO: then check that "duration" is in ctx.exception.missing
        self.assertIn("duration", ctx.exception.missing)


if __name__ == "__main__":
    unittest.main()