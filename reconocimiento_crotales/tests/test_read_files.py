import unittest

import os.path
import numpy as np

def file_format_exception(path):
    format = os.path.splitext(path)[1]
    if format != ".jpg" and format != ".TIF":
        raise Exception

class ReadFilesTest(unittest.TestCase):
    def test_read_jpg(self):
        path = './data/@__Crotal1.jpg'
        np.testing.assert_equal(
            '.jpg',
            os.path.splitext(path)[1]
        )

    def test_read_tif(self):
        path = './data/@__Crotal1.TIF'
        np.testing.assert_equal(
            '.TIF',
            os.path.splitext(path)[1]
        )

    def test_handle_invalid_format(self):
        path = './data/@__Crotal1.png'
        self.assertRaises(Exception, lambda: file_format_exception(path))

if __name__ == '__main__':
    unittest.main()