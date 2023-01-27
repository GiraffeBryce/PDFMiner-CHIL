import pdfplumber
from pdfplumber import utils

from pdfpage import PDFPage

file1 = "/Users/btw4/Desktop/Junior Year/CSCI 390/Editable Ballots/ClearBallot_paper_ballot2.pdf"
file2 = "/Users/btw4/Desktop/Junior Year/CSCI 390/Editable Ballots/CHIL bubbleballot01.pdf"
file3 = "/Users/btw4/Desktop/Junior Year/CSCI 390/Editable Ballots/ESS_paper_ballot2.pdf"
file4 = "/Users/btw4/Desktop/Junior Year/CSCI 390/Editable Ballots/Hart_paper_ballot2.pdf"
file5 = "/Users/btw4/Desktop/Junior Year/CSCI 390/Editable Ballots/Unisyn_paper_ballot2.pdf"
main_file = file4

# fp = open(file, 'rb')
# pages = PDFPage.get_pages(fp)
report = pdfplumber.open(main_file).pages[0]

im = report.to_image()

words = report.extract_words(x_tolerance=.02)

#utils.words_to_layout(words)

#im.save("/Users/btw4/Desktop/Junior Year/CSCI 390/hart extracting.png", format="PNG")