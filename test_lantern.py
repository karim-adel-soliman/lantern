import subprocess
import sys
import unittest


class LanternTests(unittest.TestCase):
    def test_empty_list_message(self):
        result = subprocess.run(
            [sys.executable, "lantern.py", "list"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "No tasks found.")


if __name__ == "__main__":
    unittest.main()