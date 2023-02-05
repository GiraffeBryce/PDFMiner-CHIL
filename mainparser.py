import pdfplumber
from mainletterparser import letter_parse

from mainpdfparser import curve_parse

from mainshapeparser import rect_parse, image_parse, line_parse

# main_file = "/Users/btw4/Desktop/Junior Year/CSCI 390/new ballots/douglas.pdf"
# main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/CHIL bubbleballot01.pdf"
# main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/Hart_paper_ballot.pdf"
# main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/ClearBallot_paper_ballot2.pdf"
# main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/Unisyn_paper_ballot.pdf"
main_file = "./sample ballots/Hart_paper_ballot.pdf"

# threshold = 35 # original
threshold = 60
bubble_found = False

im, bubble_found = curve_parse(main_file)

print ("curve parsed, bubble found? ", bubble_found)

im, bubble_found = rect_parse(main_file, im, bubble_found)

im = letter_parse(main_file, threshold, im, bubble_found)

print("letters parsed")


# im.save("/Users/btw4/Desktop/Junior Year/CSCI 390/new ballots/douglas main combo.png", format="PNG")
# im.save("/Users/shannonshao/Desktop/COMP490/Ballots/CHIL bubbleballot01.png", format="PNG")
# im.save("/Users/shannonshao/Desktop/COMP490/Ballots/Hart_paper_ballot.png", format="PNG")
# im.save("/Users/shannonshao/Desktop/COMP490/Ballots/ClearBallot_paper_ballot2.png", format="PNG")
# im.save("/Users/shannonshao/Desktop/COMP490/Ballots/Unisyn_paper_ballot.png", format="PNG")
im.save("./sample_ballots_output/hart_ballot.png", format="PNG")