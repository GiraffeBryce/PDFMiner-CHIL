import numpy as np
import pdfplumber

# Loading the file
sample_ballot = "/Users/arianawang/Documents/Rice/CHIL bubbleballot01 (1).pdf"

# Looking at the first few rows
with pdfplumber.open(sample_ballot) as pdf:
    first_page = pdf.pages[0]
    rows = first_page.extract_text().split('\n')
rows[:10]

# print("rows", rows)

# print(first_page.to_image(resolution=150).outline_words())


#report = pdfplumber.open("C:/Users/aland/Documents/Rice Documents/Rice Freshman Year/PDF Parsing/lswagenergy.pdf").pages[0]
report = pdfplumber.open(sample_ballot).pages[0]
report.curves[12]
im = report.to_image()
im.draw_lines(report.curves, stroke="red", stroke_width=2)
# im.save("/Users/arianawang/Documents/Rice/CHIL bubbleballot01 (3).png", format="PNG")


im.reset()
colors = [ "gray", "red", "blue", "green" ]
for i, curve in enumerate(report.curves):
    print(i, "curve", curve)
    stroke = colors[i%len(colors)]
    im.draw_circles(curve["points"], radius=3, stroke=stroke, fill="white")
    # im.draw_line(curve["points"], stroke=stroke, stroke_width=2)

# im.save("/Users/arianawang/Documents/Rice/CHIL bubbleballot01 TEST2.png", format="PNG")

# print(im.draw_lines(report.curves, stroke="red", stroke_width=2))
# print(len(report.curves))
# print(report.curves[12])

# Github link: https://github.com/jsvine/pdfplumber/blob/stable/examples/notebooks/ag-energy-roundup-curves.ipynb