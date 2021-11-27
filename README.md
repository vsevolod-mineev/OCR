# Tesseract OCR with CLI for JPG, PNG and PDF

OCR project with a command line interface, pre-processing and post-processing.

# How to use:
Clone this Github repository into your current directory:
```
git clone https://github.com/vsevolod-mineev/OCR .
```
To install the defined dependencies for this project use:
```
poetry install
```
To execute the command within the virtual environment use:
```
poetry run
```

Run the script using the following format:
```
poetry run python3 main.py detect --input_file='samples/jpg.jpg' --output_file='output.txt'
```
```
Options:
  --input_file ’path’         Input file to perform OCR on.
  --output_file ’path’        Output file to write strig to.
  --grayscale True            Grayscale image
  --auto_correct True         Enable OCR auto correct.
  --denoise True              Denoise image.
  --threshold True            Threshold image.
  --remove_horizontal_lines True   
  --remove_vertical_lines True 
  --dilate_bitwise_and True   Perform dilate + bitwise_and.
  --erode True                Erode image.
  --opening True              Open image. Erosion + Dilation
  --help                      Show this message and exit.
```

# How to get good results for samples:

JPG:
```
poetry run python3 main.py detect --input_file='samples/jpg.jpg' --grayscale True --denoise True --auto_correct True
```
PNG:
```
poetry run python3 main.py detect --input_file='samples/png.png' --threshold True --remove_horizontal_lines True --dilate_bitwise_and True --auto_correct True
```
PDF:
```
poetry run python3 main.py detect --input_file='samples/pdf.pdf'
```
