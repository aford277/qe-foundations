"""qe_foundations/ingestion/contexts.py  -  TASK 3 (about 25 min)

Two context managers:
  * open_source(path)  - generator style (@contextmanager)
  * LoadSession(path)  - class style (__enter__ / __exit__)

See README Task 3 for the exact behaviour required.
"""

import time
from contextlib import contextmanager
from pathlib import Path

from .exceptions import MalformedSourceError, SourceNotFoundError, SourceUnreadableError


@contextmanager
def open_source(path):
    """Open a text file for reading and translate low-level errors into ours.

    Requirements (README Task 3A):
      * encoding "utf-8-sig" (drops the Excel BOM) and newline="" (csv module).
      * missing file                     -> SourceNotFoundError   (keep the cause: `from error`)
      * any other OSError on open        -> SourceUnreadableError (keep the cause)
      * UnicodeDecodeError while reading -> MalformedSourceError  (keep the cause)
      * the file is ALWAYS closed, even when the with-body raises.
    """
    try:
        file = open(path, "r", encoding="utf-8-sig", newline="")
    except FileNotFoundError as error:
        raise SourceNotFoundError(path) from error
    except OSError as error:
        raise SourceUnreadableError(path, error) from error

    try:
        yield file
    except UnicodeDecodeError as error:
        raise MalformedSourceError(path, f"invalid encoding ({error.reason})") from error
    finally:
        file.close()

class LoadSession:
    """Bookkeeping around one load (README Task 3B).

    After the `with` block ends:
      * .outcome  is "completed" or "failed"
      * .elapsed  is the number of seconds the block took (float, >= 0)
    It must NEVER swallow an exception raised inside the block.
    """

    def __init__(self, path):
        self.path = Path(path)
        self.outcome = None
        self.elapsed = None

    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start

        if exc_type is None:
            self.outcome = "completed"
        else:
            self.outcome = "failed"

        return False if self.outcome == "failed" else None