import unittest
from unittest.mock import mock_open, create_autospec, patch
from zad1.src.fileManager import FileManager

class TestApp(unittest.TestCase):
    def setUp(self):
        self.temp = FileManager()

    def test_read_file(self):
        with patch('builtins.open', mock_open(read_data="data from file...")):
            self.assertEqual(self.temp.readFile('file.txt'), "data from file...")

    def test_add_line_to_file(self):
        with patch('builtins.open', mock_open(read_data="some data")) as mockfile:
            self.temp.addLineToFile("file.txt", "and some other data")
            mockfile.assert_called_once_with("./file.txt", "r")

    def test_delete_file(self):
        mock_function = create_autospec(self.temp)
        mock_function.deleteFile("file.txt")
        mock_function.deleteFile.assert_called_once_with("file.txt")

    def tearDown(self):
        self.app = None


if __name__ == "__main__":
    unittest.main()