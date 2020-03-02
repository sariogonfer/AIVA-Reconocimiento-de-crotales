import unittest

import cv2
import numpy as np

class EarTagIdentifierMock:
    def extract_number(self, raw_img):
        if np.array_equal(raw_img, cv2.imread('./data/__Crotal10.jpg')):
            raise Exception
        for i in range(1, 10):
            img = cv2.imread(f'./data/__Crotal{i}.jpg', 0)
            if np.array_equal(raw_img, img):
                return cv2.imread(f'./data/@__Crotal{i}.jpg', 0)

    def read_number(self, img):
        return 1225


class EarTagIdentifierTest(unittest.TestCase):
    def setUp(self):
        self.ear_tag_identifier = EarTagIdentifierMock()

    def test_extract_number(self):
        for i in range(1, 10):
            expected_img = cv2.imread(f'./data/@__Crotal{i}.jpg', 0)
            raw_img = cv2.imread(f'./data/__Crotal{i}.jpg',  0)
            np.testing.assert_array_equal(
                expected_img,
                self.ear_tag_identifier.extract_number(raw_img)
            )

    def test_read_number(self):
        raw_img = cv2.imread('./data/@__Crotal1.jpg', 0)
        self.assertEqual(
            1225,
            self.ear_tag_identifier.read_number(raw_img)
        )

    def test_handle_invalid_img(self):
        raw_img = cv2.imread('./data/__Crotal10.jpg')
        self.assertRaises(
            Exception,
            lambda: self.ear_tag_identifier.extract_number(raw_img)
        )

if __name__ == '__main__':
    unittest.main()
