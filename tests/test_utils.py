import unittest
from datetime import date

from qe_foundations.utils import add_days, is_valid_email, percent, slugify


class TestStrings(unittest.TestCase):

    # ---- 1. Normal case, table-driven with subTest -------------------------
    def test_slugify_turns_titles_into_lowercase_dashed_slugs(self):
        cases = [
            ("  Login Page: Happy Path ", "login-page-happy-path"),
            ("Search", "search"),
            (" WOrking . tree", "working-tree")
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(slugify(text), expected)

    # ---- 2. Normal case: True and False results ---------------------------
    def test_is_valid_email_accepts_good_and_rejects_bad_addresses(self):
        self.assertTrue(is_valid_email("adam@example.com"))
        self.assertFalse(is_valid_email("bob.example.com"))
        self.assertFalse(is_valid_email("charlie@example@com"))
        self.assertFalse(is_valid_email("david@examplecom"))


class TestNumbers(unittest.TestCase):

    # ---- 3. Normal case + the zero edge case ------------------------------
    def test_percent_rounds_to_one_decimal_and_zero_whole_gives_zero(self):
        self.assertAlmostEqual(percent(1, 3), 33.3)
        self.assertAlmostEqual(percent(93, 100), 93.0)
        self.assertEqual(percent(5, 0), 0)


class TestDates(unittest.TestCase):

    # ---- 4. Bad input with assertRaises -----------------------------------
    def test_add_days_with_string_date_raises_type_error(self):
        # Arrange: a date given as text instead of a datetime.date
        not_a_date = "2026-10-23"

        with self.assertRaises(TypeError):
            add_days(not_a_date, 1)

if __name__ == "__main__":
    unittest.main()