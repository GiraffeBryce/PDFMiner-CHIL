from converter import PDFPageAggregator
from layout import LAParams, LTComponent, LTCurve, LTImage, LTLine, LTRect, LTText, LTTextBox, LTTextLine
from mainpdfparser import is_letter
from pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfpage import PDFPage
import pdfplumber


file1 = "/Users/btw4/Desktop/Junior Year/CSCI 390/Editable Ballots/ClearBallot_paper_ballot2.pdf"

main_file = file1

fp = open(main_file, 'rb')

report = pdfplumber.open(main_file).pages[0]

im = report.to_image()

im.save("/Users/btw4/Desktop/Junior Year/CSCI 390/clear fix/clear compression.png", format="PNG")
