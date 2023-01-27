# RECT_PARSE

from cmath import inf
import pdfplumber

from pdfpage import PDFPage

# main_file = "/Users/btw4/Desktop/Junior Year/CSCI 390/new ballots/san miguel.pdf"
# main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/CHIL bubbleballot01.pdf"
# main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/Hart_paper_ballot.pdf"
# main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/ClearBallot_paper_ballot2.pdf"
# main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/Unisyn_paper_ballot.pdf"
main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/ESS_paper_ballot2.pdf"

fp = open(main_file, 'rb')
pages = PDFPage.get_pages(fp)
sample_ballot = main_file

# Choosing page of ballot to run the code. Input different index for diff pages.
repo = pdfplumber.open(sample_ballot).pages[0]
# Create the image to save
im = repo.to_image()

height = 0
num = 0

for page in pages:
    if num >= 1:
        break
    height1 = page.mediabox[1]
    height2 = page.mediabox[3]
    height = abs(height2-height1)
    num += 1


def rect_parse(file, image, bubble_found):
    report = pdfplumber.open(file).pages[0]
    im = image
    height = 0
    num = 0

    for page in pages:
        if num >= 1:
            break
        height1 = page.mediabox[1]
        height2 = page.mediabox[3]
        height = abs(height2-height1)
        num += 1

    if (bubble_found):
        shortest_diag = -1
    else:
        shortest_diag = inf

    diag_count = 0

    # Iterate through the detected rectangles
    for i, rect in enumerate(report.rects):
        # If the curve detected is not a line (i.e. two points on the curve detected)
        diag = (abs(rect['x0'] - rect['x1'])**2) + (abs(rect['y0'] - rect['y1'])**2)
        # im.draw_line(((rect['x0'], height-rect['y0']), (rect['x1'], height-rect['y1'])), stroke = "red")
        #print("rect found with diagonal ", diag)
        if (diag < shortest_diag):
            shortest_diag = diag
        # for later: can assume that the smallest rectangles on the page are the voting bubbles:
        # find the smallest first, then check the rectangles against that heuristic to find ones of 
        # comparable size

    # Iterate through the detected rectangles
    for i, rect in enumerate(report.rects):
        diag = (abs(rect['x0'] - rect['x1'])**2) + (abs(rect['y0'] - rect['y1'])**2)
        if (abs(shortest_diag - diag) < 0.2):
            im.draw_line(((rect['x0'], height-rect['y0']), (rect['x1'], height-rect['y1'])), stroke = "red")
            print("red line drawn")
            diag_count += 1
        else:
            im.draw_line(((rect['x0'], height-rect['y0']), (rect['x1'], height-rect['y1'])), stroke = "gray")
            print("gray line drawn")
    if diag_count > 1:
        bubble_found = True
    return im, bubble_found

print("continuing...")
for i, curve in enumerate(repo.curves):
    print("curve found!")
    im.draw_line(((curve['x0'], height-curve['y0']), (curve['x1'], height-curve['y1'])), stroke = "orange")

print("continuing...")
def image_parse(file, im):
    height = 0
    num = 0

    for page in pages:
        if num >= 1:
            break
        height1 = page.mediabox[1]
        height2 = page.mediabox[3]
        height = abs(height2-height1)
        num += 1
    report = pdfplumber.open(file).pages[0]
    for i, image in enumerate(report.images):
        print("image found!")
        im.draw_line(((image['x0'], height-image['y0']), (image['x1'], height-image['y1'])), stroke = "yellow")
    return im

print("continuing...")
def line_parse(file, im):
    height = 0
    num = 0

    for page in pages:
        if num >= 1:
            break
        height1 = page.mediabox[1]
        height2 = page.mediabox[3]
        height = abs(height2-height1)
        num += 1
    report = pdfplumber.open(file).pages[0]
    for i, line in enumerate(report.lines):
        print("line found!")
        im.draw_line(((line['x0'], height-line['y0']), (line['x1'], height-line['y1'])), stroke = "green")
    return im

print("continuing...")
for i, anno in enumerate(repo.annots):
    print("anno found!")
    im.draw_line(((anno['x0'], height-anno['y0']), (anno['x1'], height-anno['y1'])), stroke = "blue")


#im.save("/Users/btw4/Desktop/Junior Year/CSCI 390/new ballots/rect bubble san miguel.png", format="PNG")