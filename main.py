import sys
sys.path.append('/Users/vsevolod_mineev/miniconda3/lib/python3.9/site-packages')
from PIL2CV import PIL2CV
from preprocess import preprocess
from file_type_detector import FileTypeDetector
from imageConverter import ImageConverter
import pytesseract
import fire
def text_detect(input_file="samples/pdf.pdf",output_file = "output.txt",grayscale=False,auto_correct=False,denoise=False,threshold=False,remove_horizontal_lines=False,remove_vertical_lines=False,dilate_bitwise_and=False,erode=False,opening=False):
    print("OCR has started")
    image_array = ImageConverter(input_file).convert()
    length = len(image_array)
    x=range(length)   
    for i in x:
        image_data= PIL2CV.pil_to_cv(image_array[i])
        # applying preprocessing to image_data given that it has been specified as an a desired option to the script.
        if grayscale is True:
            image_data = preprocess.cv_grayscale(image_data)
        if denoise is True:
            image_data = preprocess.cv_no_noise(image_data)
        if threshold is True:
            image_data = preprocess.cv_threshold(image_data)
        if remove_horizontal_lines is True:
            image_data = preprocess.cv_remove_horizontal_lines(image_data)
        if remove_vertical_lines is True:
            image_data = preprocess.cv_remove_vertical_lines(image_data)
        if dilate_bitwise_and is True:
            image_data = preprocess.cv_dilate_bitwise_and(image_data,input_file)
        if erode is True:
            image_data = preprocess.cv_erode(image_data)
        if opening is True:
            image_data = preprocess.cv_opening(image_data)
        image_array[i] = image_data

    # using pytesseract to perform OCR and get a string for each page and merging these strings together to get the final result
    result = str()
    for i in x:
        result = result + str(pytesseract.image_to_string(image_array[i]))

    # applying postprocessing  
    if auto_correct is True:
        result = preprocess.spell_correct_ocr(result)
    # writing output
    text_file = open(output_file, "w")
    text_file.write(result)
    text_file.close()
    print("OCR has finished")

class Pipeline(object):
    def __init__(self):
        self.detect = text_detect

if __name__ == "__main__":
    fire.Fire(Pipeline)
