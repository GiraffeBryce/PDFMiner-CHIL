import numpy as np
import pdfplumber

# Loading the file
sample_ballot = "/Users/arianawang/Documents/Rice/Sample/CHIL bubbleballot01 (1).pdf"
# Choosing page of ballot to run the code
report = pdfplumber.open(sample_ballot).pages[0]
# Create the image to save
im = report.to_image()

# Colors that the coordinates will be mapped in
colors = [ "gray", "red", "blue", "green" ]

# Iterate through the detected curves
for i, curve in enumerate(report.curves):
    # If the curve detected is not a line (i.e. two points on the curve detected)
    if len(curve["points"]) != 2:
        # The color chosen
        stroke = colors[i%len(colors)]
        x_values = 0
        y_values = 0
        # Sums up the values of the curves
        for points in curve["points"]:
            x_values += points[0]
            y_values += points[1] 
        # Calculates the midpoint of the bubble
        midpoint = [(round((x_values/len(curve["points"]))), round((y_values/len(curve["points"]))))]
        # Marks the curve
        im.draw_circles(midpoint, radius=3, stroke=stroke, fill="white")

# Saves the new ballot
im.save("/Users/arianawang/Documents/Rice/Sample/CHIL bubbleballot01 testthree.png", format="PNG")

# Github link: https://github.com/jsvine/pdfplumber/blob/stable/examples/notebooks/ag-energy-roundup-curves.ipynb