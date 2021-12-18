from setuptools import setup
setup(
    name='OCR-pdf-jpg-png',
    version='0.9.0',
    description="Tesseract OCR with OpenCV preprocessing and auto-correct.",
    long_description="",
    author='Vsevolod Mineev',
    author_email='vsevolod.mineev@gmail.com',
    url='https://github.com/vsevolod-mineev/md5-brute-force',
    license='MIT',
    entry_points={'console_scripts': ['OCR = main:text_detect']},
)