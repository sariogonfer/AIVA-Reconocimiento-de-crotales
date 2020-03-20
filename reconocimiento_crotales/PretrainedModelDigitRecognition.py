from reconocimiento_crotales.BaseDigitRecognition import BaseDigitRecognition


class PretrainedModelDigitRecognition(BaseDigitRecognition):
    def predict(self, image, rois):
        text=""
        for r in rois:
            text=text+super().predict(image, r[0], r[1])
            (startX, startY) = r[0]
            (endX, endY) = r[1]

            if platform.system()=="Windows":
                # Need to specify the path only in widows systems
                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

            roi = image[startY:endY, startX:endX]
            config = ("-l eng --oem 1 --psm 7 -c tessedit_char_whitelist=0123456789")
            text_ = pytesseract.image_to_string(roi, config=config)

            if text_ == "":
                raise ExceptionNotDigitRecognized()
            text += text_
        return text

    def model(self):
        #TO DO: Implementar conexión con rrnn MNIST para mejorar resultados
        return None
