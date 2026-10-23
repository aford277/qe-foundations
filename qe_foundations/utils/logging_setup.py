"""
qe_foundations/utils/logging_setup.py   (Project 1 milestone, Part E: copy this file into your repo)

Contract (the self-check script tests exactly this):
    setup_logging(level="INFO", logfile=None) -> logging.Logger
      * configures the logger named "qe_foundations" (the parent of every module logger in the package)
      * console handler at `level`; if `logfile` is given, also a file handler that records DEBUG and up
      * safe to call twice: it must NOT add duplicate handlers
      * returns the "qe_foundations" logger
Call it ONCE, from your entry point (a script or main()), never at import time in a library module.
"""
import logging
import sys


def setup_logging(level="INFO", logfile=None):
    # 1: get the logger named "qe_foundations" and set its level to DEBUG (gate 1)
    # 2: if it already has handlers, return it unchanged (idempotent)
    # 3: build a Formatter: time | level | logger name | message
    # 4: console StreamHandler(sys.stdout) at `level` (gate 2)
    # 5: if logfile: FileHandler(logfile, encoding="utf-8") at DEBUG
    logger = logging.getLogger("qe_foundations")
    logger.setLevel(logging.DEBUG)                     # gate 1: let everything through

    if logger.handlers:                                # idempotent
        return logger

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    console = logging.StreamHandler(sys.stdout)
    console.setLevel(level)                            # gate 2: console filters
    console.setFormatter(formatter)
    logger.addHandler(console)

    if logfile:
        fh = logging.FileHandler(logfile, encoding="utf-8")
        fh.setLevel(logging.DEBUG)                     # file keeps full detail
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
