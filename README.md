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
poetry run python3 detect main.py --input_file='samples/jpg.jpg' --output_file='output.txt'
```
```
Options:
  --input_file=’path’         Input file to perform OCR on.
  --output_file=’path’        Output file to write strig to.
  --log_file=’path’           File where the logs should go.
  --verbose                   Output detailed logs for this OCR.
  --grayscale                 Grayscale image
  --auto_correct              Enable OCR auto correct.
  --denoise                   Denoise image.
  --threshold                 Threshold image.
  --remove_horizontal_lines   Remove horizontal lines on image.
  --remove_vertical_lines     Remove vertical lines from image.
  --dilate_bitwise_and        Perform dilate + bitwise_and.
  --erode                     Erode image.
  --opening                   Open image. Erosion + Dilation
  --help                      Show this message and exit.
```

# How to get good results for samples:

JPG:
```
python3 code_test.py --input_file='samples/jpg.jpg' --grayscale --denoise --auto_correct
```
PNG:
```
python3 code_test.py --input_file='samples/png.png' --grayscale --threshold --remove_horizontal_lines --dilate_bitwise_and --auto_correct
```
PDF:
```
python3 code_test.py --input_file='samples/pdf.pdf'
```
