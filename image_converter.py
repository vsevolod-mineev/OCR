from pathlib import Path

from pdf2image import convert_from_path
from PIL import Image
from podder_task_foundation.exceptions import PodderTaskException

from .file_type_detector import FileTypeDetector


class ImageConverter(object):
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def convert(self) -> []:
        images = []
        filetype = FileTypeDetector(self.file_path).detect()
        if filetype == FileTypeDetector.FILETYPE_PDF:
            images = convert_from_path(self.file_path)
            print("Detected filetype: PDF, " + str(len(images)) + " page(s)")
        elif filetype in [
                FileTypeDetector.FILETYPE_JPEG, FileTypeDetector.FILETYPE_PNG,
                FileTypeDetector.FILETYPE_TIFF
        ]:
            images.append(Image.open(self.file_path))
            print("Detected filetype: " + filetype)
        else:
            raise PodderTaskException(
                "Unsupported File Type", "This task can accept PDF, TIFF, JPEG, PNG only",
                "Check your input file and convert it into the supported file types.")

        return images
