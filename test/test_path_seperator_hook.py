import os.path
import unittest
import shutil
from parameterized import parameterized
from hooks.check_paths import check_for_path_seperator

class TestPathSeperatorHook(unittest.TestCase):

    test_parameters = ([
        ("test_simple_string", "This is a string", 0),# noqa
        ("test_simple_string_with_backslash", "This is a string test with \\", 0),# noqa
        ("test_simple_string_with_slash", "This is a string test with /", 0),# noqa
        ("test_unix_path_trailing_slash", "This/is/a/path/", 1),# noqa
        ("test_unix_path", "This/is/a/path", 1),# noqa
        ("test_windows_path_trailing_backslash", "This\is\\a\path\\", 1),# noqa
        ("test_windows_path", "This\is\\a\path", 1),# noqa
        ("test_https_url", "https://This/is/a/url", 0),# noqa
        ("test_http_url", "http://This/is/a/url", 0),# noqa
        ("test_not_http_url", "http/This/is/not/a/url", 1),# noqa
        ("test_not_https_url", "https:/This/is/not/a/url", 1),# noqa
        ("test_simple_string_with_new_line", "This is a string with new line \n ", 0),# noqa
    ])

    #os.sep +


    path_10 = ""
    test_directory_path = os.path.join("tmp" , "path_seperator_test_environment")
    test_file = test_directory_path + os.sep + "path_test_python_file.py"

    def setUp(self) -> None:
        if os.path.exists(self.test_directory_path):
            shutil.rmtree(self.test_directory_path)
        os.makedirs(self.test_directory_path, exist_ok=False)

    # def tearDown(self) -> None:
    #     if os.path.exists(self.test_directory_path):
    #         shutil.rmtree(self.test_directory_path)

    def create_test_python_file(self, variable_value:str):
        file_content = f"test_variable = {repr(variable_value)}\n"

        with open(self.test_file, "w") as file:
            file.write(file_content)

    @parameterized.expand(test_parameters)
    def test_hook(self, _, test_string, expected_code):
        self.create_test_python_file(variable_value=test_string)

        exit_code = check_for_path_seperator(self.test_file)

        self.assertEqual(exit_code, expected_code, msg=f"{test_string} should return exit code {expected_code}:" +(("hard codded path detected") if expected_code == 1 else "no hardcoded path detected"))

