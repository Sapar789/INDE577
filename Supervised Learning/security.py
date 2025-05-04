import sys
import os
import contextlib

@contextlib.contextmanager
def suppress_stderr():
    stderr = sys.stderr
    sys.stderr = open(os.devnull, 'w')
    try:
        yield
    finally:
        sys.stderr = stderr
