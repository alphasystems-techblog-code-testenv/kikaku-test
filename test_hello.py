import unittest
from io import StringIO
from contextlib import redirect_stdout

from hello import get_message, main


class TestHello(unittest.TestCase):
    def test_get_message(self):
        self.assertEqual(get_message(), "Hello, GitLab project!")
        self.assertEqual(get_message("world"), "Hello, world!")

    def test_main_default_output(self):
        output = StringIO()
        with redirect_stdout(output):
            main("GitLab project")
        self.assertEqual(output.getvalue().strip(), "Hello, GitLab project!")

    def test_main_custom_target_output(self):
        output = StringIO()
        with redirect_stdout(output):
            main("custom target")
        self.assertEqual(output.getvalue().strip(), "Hello, custom target!")

if __name__ == "__main__":
    unittest.main()
