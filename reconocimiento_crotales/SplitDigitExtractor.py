from imutils.object_detection import non_max_suppression
import cv2
import numpy as np
import os

from reconocimiento_crotales.ExceptionNotDigitDetected import ExceptionNotDigitDetected
from reconocimiento_crotales.BaseDigitExtractor import BaseDigitExtractor

# Clase que se dedica a la extracción de dígitos a partir de una imagen dada
class SplitDigitExtractor(BaseDigitExtractor):

    # Método que detecta las lineas de caracteres de una imagen, y devuelve la mejor candidata a albergar el identificador
    #
    # params
    # image: imagen de la que se extraerán los dígitos
    #
    # return
    # image: imagen una vez preprocesada
    # best_bb_start: coordenadas (x,y) del inicio del mejor bbox candidato a albergar el identificador
    # best_bb_end: coordenadas (x,y) del final del mejor bbox candidato a albergar el identificador
    def detect_boundaries(self, image):
        image = self.preprocess_image(image)

        min_confidence = 0.5
        # The EAST text requires that your input image dimensions be multiples of 32, so if you choose to adjust your --width and --height values, make sure they are multiples of 32!
        height = 320
        width = 320
        padding = 0.0
        east = os.path.join(
            os.path.dirname(__file__), 'models/frozen_east_text_detection.pb'
        )
        (origH, origW) = image.shape[:2]

        (newW, newH) = (width, height)
        rW = origW / float(newW)
        rH = origH / float(newH)

        image_r = cv2.resize(image, (newW, newH))
        (H, W) = image_r.shape[:2]

        layerNames = [
            "feature_fusion/Conv_7/Sigmoid",
            "feature_fusion/concat_3"]

        net = cv2.dnn.readNet(east)

        blob = cv2.dnn.blobFromImage(image_r, 1.0, (W, H), (123.68, 116.78, 103.94), swapRB=True, crop=False)
        net.setInput(blob)
        (scores, geometry) = net.forward(layerNames)

        (rects, confidences) = self.__decode_predictions(scores, geometry, min_confidence)
        boxes = non_max_suppression(np.array(rects), probs=confidences)

        best_bb_start = (0, 0)
        best_bb_end = (0, 0)
        for (startX, startY, endX, endY) in boxes:
            startX = int(startX * rW)
            startY = int(startY * rH)
            endX = int(endX * rW)
            endY = int(endY * rH)

            dX = int((endX - startX) * padding)
            dY = int((endY - startY) * padding)

            startX = max(0, startX - dX)
            startY = max(0, startY - dY)
            endX = min(origW, endX + (dX * 2))
            endY = min(origH, endY + (dY * 2))
            #cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)


            if endY > best_bb_end[1]:
                best_bb_start = (startX, startY)
                best_bb_end = (endX, endY)
        #cv2.rectangle(image, best_bb_start, best_bb_end, (0, 0, 255), 2)
        #cv2.imshow("Best bb", image)
        #cv2.waitKey(0)

        if best_bb_start==best_bb_end:
            raise ExceptionNotDigitDetected()
            return None
        else:
            return image, best_bb_start, best_bb_end


    # Método interno utilizado por detect_boundaries que sirve para identificar si las lineas de caracteres detectadas cumplen unos mínimos
    # param
    # scores: bboxes candidatos
    # geometry: valores generados por la red detectora
    # min_confidence: escalar que sirve como cota
    #
    # return
    # rects: posiciones de la bbox
    # confidences: puntuaciones de la bbox en el estudio
    def __decode_predictions(self, scores, geometry, min_confidence):
        (numRows, numCols) = scores.shape[2:4]
        rects = []
        confidences = []

        for y in range(0, numRows):
            scoresData = scores[0, 0, y]
            xData0 = geometry[0, 0, y]
            xData1 = geometry[0, 1, y]
            xData2 = geometry[0, 2, y]
            xData3 = geometry[0, 3, y]
            anglesData = geometry[0, 4, y]

            for x in range(0, numCols):
                if scoresData[x] < min_confidence:
                    continue

                (offsetX, offsetY) = (x * 4.0, y * 4.0)

                angle = anglesData[x]
                cos = np.cos(angle)
                sin = np.sin(angle)

                h = xData0[x] + xData2[x]
                w = xData1[x] + xData3[x]

                endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
                endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
                startX = int(endX - w)
                startY = int(endY - h)

                rects.append((startX, startY, endX, endY))
                confidences.append(scoresData[x])

        return (rects, confidences)

    # Método que se encarga del preprocesado de la imagen
    # params
    # image: imagen que será procesada
    #
    # return
    # image: imagen una vez preprocesada
    def preprocess_image(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_val = np.array([0, 0, 0])
        upper_val = np.array([179, 255, 80])
        mask = cv2.inRange(hsv, lower_val, upper_val)
        masked = cv2.bitwise_not(mask)
        image= cv2.cvtColor(masked,cv2.COLOR_GRAY2RGB)
        kernel = np.ones((5, 5), np.uint8)
        image = cv2.erode(image, kernel, iterations=1)
        return cv2.dilate(image, kernel, iterations=1)

    # Método que se encarga de la extracción de los dígitos
    # params
    # image: imagen que será procesada
    #
    # return
    # image_orig: imagen una vez preprocesada
    # rois: lista que contiene todas los bbox de los dígitos detectados
    def extract_digits(self, image):
        image, bb_start, bb_end = self.detect_boundaries(image)

        image_orig=np.copy(image)
        image = image[bb_start[1]:bb_end[1], bb_start[0]:bb_end[0]]
        image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        edges = cv2.adaptiveThreshold(image_grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, -2)
        # cv2.imshow("edges", edges)
        # cv2.waitKey(0)

        kernel = np.ones((1, 2), dtype="uint8")
        dilated = cv2.dilate(edges, kernel)
        im2, ctrs, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # sort contours
        sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

        # maxsize_rois=4
        all_rois = []
        rois = []
        for i, ctr in enumerate(sorted_ctrs):
            # Get bounding box
            x, y, w, h = cv2.boundingRect(ctr)
            roi = image[y:y + h, x:x + w]

            if w + h > 120 and w > 45 and h > 90:
                rois.append([(bb_start[0]+x, bb_start[1]+y), (bb_start[0]+x+w, bb_start[1]+y+h)])

        return image_orig, rois
