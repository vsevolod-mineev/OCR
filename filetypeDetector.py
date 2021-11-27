from pathlib import Path


class filetypeDetector(object):
    FILETYPE_PDF = 'pdf'
    FILETYPE_TIFF = 'tiff'
    FILETYPE_JPEG = 'jpeg'
    FILETYPE_PNG = 'png'

    def __init__(self, file_path: str):
        self.file = Path(file_path)

    def detect(self):
        file_handle = open(self.file.resolve(), "rb")
        try:
            byte = file_handle.read(10)
        finally:
            file_handle.close()

        # PDF
        if byte[0:4] == b'%PDF':
            return self.FILETYPE_PDF

        # TIFF
        if byte[0:4] == b'\x4D\x4D\x00\x2A' or \
                byte[0:4] == b'\x4D\x4D\x00\x2B' or \
                byte[0:4] == b'\x49\x49\x2A\x00' or \
                byte[0:4] == b'\x49\x49\x2B\x00':
            return self.FILETYPE_TIFF

        # JPEG
        if byte[0:2] == b'\xFF\xD8':
            return self.FILETYPE_JPEG

        # PNG
        if byte[0:8] == b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A':
            return self.FILETYPE_PNG

        return None