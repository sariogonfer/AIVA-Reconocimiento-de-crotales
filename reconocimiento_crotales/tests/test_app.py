import unittest

import os.path
import numpy as np

from reconocimiento_crotales.PretrainedReader import PretrainedReader

class AppTest(unittest.TestCase):
    def test_read_jpg(self):
        reader = PretrainedReader()
        identifier = reader.process_image(
            os.path.join(os.path.dirname(__file__), '0055.TIF')
        )
        assert identifier.get_value() == '55'


if __name__ == '__main__':
    unittest.main()
