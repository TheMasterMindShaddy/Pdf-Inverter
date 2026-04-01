from pdf2image import convert_from_path
from PIL import Image, ImageOps
import img2pdf
import os

input_pdf = "1.pdf"
output_pdf = "inverted_output.pdf"

POPPLER_PATH = r"D:\Codes\PDF Inverter\poppler-25.12.0\Library\bin" 

pages = convert_from_path(input_pdf, dpi=200, poppler_path=POPPLER_PATH)

inverted_images = []
for i, page in enumerate(pages):
    inverted = ImageOps.invert(page.convert("RGB"))
    temp_name = f"inverted_page_{i}.jpg"
    inverted.save(temp_name)
    inverted_images.append(temp_name)

with open(output_pdf, "wb") as f:
    f.write(img2pdf.convert(inverted_images))

for img in inverted_images:
    os.remove(img)

print("Done!")
