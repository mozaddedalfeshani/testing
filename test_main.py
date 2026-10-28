import subprocess
import sys
import unittest
from pathlib import Path

MAIN = Path(__file__).with_name("main.py")


class TestMain(unittest.TestCase):
    def test_main_runs_cleanly(self):
        result = subprocess.run(
            [sys.executable, "-I", str(MAIN)],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "\n")


if __name__ == "__main__":
    unittest.main()
