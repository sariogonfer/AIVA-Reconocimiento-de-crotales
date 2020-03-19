import cv2
import numpy as np
import pytesseract
from reconocimiento_crotales.ExceptionNotDigitRecognized import ExceptionNotDigitRecognized
import platform

class BaseDigitRecognition():
    def predict(self, image, bb_start, bb_end):
        (startX, startY) = bb_start
        (endX, endY) = bb_end

        if platform.system()=="Windows":
            # Need to specify the path only in widows systems
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        roi = image[startY:endY, startX:endX]
        config = ("-l eng --oem 1 --psm 7 -c tessedit_char_whitelist=0123456789")
        text = pytesseract.image_to_string(roi, config=config)

        if text=="":
            raise ExceptionNotDigitRecognized()

        # print(startX, startY, endX, endY)
        # print("{}\n".format(text))
        """
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
        cv2.putText(image, text, (startX, startY - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

        cv2.imshow("Text Detection", image)
        cv2.waitKey(0)
        """
        return text