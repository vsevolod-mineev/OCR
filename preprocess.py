import sys
sys.path.append('/Users/vsevolod_mineev/miniconda3/lib/python3.9/site-packages')
from pdf2image import convert_from_path, convert_from_bytes
import cv2
class preprocess(object):
    def __init__(self):
        self.name = "preprocess"

    def grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # auto correct that only corrects substitutions.
    def spell_correct_ocr(data):
        spell = Speller(only_replacements=True)
        data=spell(data)
        return data

    # removes horizotal lines from image.
    def cv_remove_horizontal_lines(image):
        horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (35,1))
        detect_horizontal = cv2.morphologyEx(image, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
        cnts = cv2.findContours(detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            cv2.drawContours(image, [c], -1, (0,0,0), 2)
        return image

    # removes vertical line from image.
    def cv_remove_vertical_lines(image):
        vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,15))
        detect_vertical = cv2.morphologyEx(image, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
        cnts = cv2.findContours(detect_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            cv2.drawContours(image, [c], -1, (0,0,0), 3)
        return image
        
    # noise removal
    def cv_no_noise(image):
        return cv2.medianBlur(image,5)
    
    # thresholding
    def cv_threshold(image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # dilation + bitwise_and
    def cv_dilate_bitwise_and(image):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10,1))
        dilate = cv2.dilate(image, kernel, iterations=2)
        cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            area = cv2.contourArea(c)
            if area < 500:
                cv2.drawContours(dilate, [c], -1, (0,0,0), -1)

        # Bitwise-and to reconstruct image
        original=cv2.imread(input_name)
        result = cv2.bitwise_and(original, original, mask=dilate)
        result[dilate==0] = (255,255,255)
        return result
        
    # erosion
    def cv_erode(image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.erode(image, kernel, iterations = 1)

    # opening - erosion followed by dilation
    def cv_opening(image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    # convert pdf to jpg
    def pdf_convert(path):
        image = convert_from_path(path, fmt='jpg')
        return image