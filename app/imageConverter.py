from pathlib import Path

from pdf2image import convert_from_path
from PIL import Image

from filetypeDetector import filetypeDetector


class ImageConverter(object):
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def convert(self) -> []:
        images = []
        filetype = filetypeDetector(self.file_path).detect()
        if filetype == filetypeDetector.FILETYPE_PDF:
            images = convert_from_path(self.file_path)
            print("Detected filetype: pdf, " + str(len(images)) + " page(s)")
        elif filetype in [
                filetypeDetector.FILETYPE_JPEG, filetypeDetector.FILETYPE_PNG,
                filetypeDetector.FILETYPE_TIFF
        ]:
            images.append(Image.open(self.file_path))
            print("Detected filetype: " + filetype)
        else:
            print(
                "Unsupported File Type", "This task can accept PDF, TIFF, JPEG, PNG only",
                "Check your input file and convert it into the supported file types.")

        return images
