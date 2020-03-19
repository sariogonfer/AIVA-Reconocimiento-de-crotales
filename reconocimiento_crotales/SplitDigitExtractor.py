from reconocimiento_crotales.BaseDigitExtractor import BaseDigitExtractor
import cv2
import numpy as np


class SplitDigitExtractor(BaseDigitExtractor):
    def detect_boundaries(self, image):
        image, bb_start, bb_end =super().extract_digits(image)

        image_orig=np.copy(image)
        image = image[bb_start[1]:bb_end[1], bb_start[0]:bb_end[0]]
        image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        edges = cv2.adaptiveThreshold(image_grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, -2)
        # cv2.imshow("edges", edges)
        # cv2.waitKey(0)

        kernel = np.ones((1, 2), dtype="uint8")
        dilated = cv2.dilate(edges, kernel)
        im2, ctrs, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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
                #cv2.rectangle(image_orig, (x, y), (x+w, y+h), (0, 0, 255), 2)
                #cv2.rectangle(image_orig, (bb_start[0]+x, bb_start[1]+y), (bb_start[0]+x+w, bb_start[1]+y+h), (0, 0, 255), 2)
                # print(x, y, w, h)

        #cv2.imshow("roii", image_orig)
        #cv2.waitKey(0)

        return image_orig, rois

    def preprocess_image(self, image):
        return super().preprocess_image(image)
