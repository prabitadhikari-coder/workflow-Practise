import io
import unittest
from contextlib import redirect_stdout

from main import print_hi


class PrintHiTests(unittest.TestCase):
    def test_print_hi_outputs_expected_greeting(self):
        output = io.StringIO()
        with redirect_stdout(output):
            print_hi("PyCharm")

        self.assertEqual(output.getvalue(), "Hi, PyCharm\n")
