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
    stroke = colors[i%len(colors)]
    x_values = 0
    y_values = 0
    for points in curve["points"]:
        x_values += points[0]
        y_values += points[1] 
    midpoint = [(curve["width"]/2 + curve["x0"], curve["height"]/2 + curve["y0"])]
    midpoint = [(round((x_values/len(curve["points"]))), round((y_values/len(curve["points"]))))]
    print("midpoint", midpoint)
    im.draw_circles(midpoint, radius=3, stroke=stroke, fill="white")
    # im.draw_line(curve["points"], stroke=stroke, stroke_width=2)

im.save("/Users/arianawang/Documents/Rice/CHIL bubbleballot01 TEST5.png", format="PNG")

# print(im.draw_lines(report.curves, stroke="red", stroke_width=2))
# print(len(report.curves))
# print(report.curves[12])

# Github link: https://github.com/jsvine/pdfplumber/blob/stable/examples/notebooks/ag-energy-roundup-curves.ipynb