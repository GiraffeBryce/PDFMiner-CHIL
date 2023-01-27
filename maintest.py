# code for visual layout analysis

from pdfminer.layout import LAParams                                                                                                                                                                                                                            
from pdfminer.converter import PDFResourceManager, PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFPageInterpreter

# main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/CHIL bubbleballot01.pdf"
# main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/Hart_paper_ballot.pdf"
# main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/ClearBallot_paper_ballot2.pdf"
# main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/Unisyn_paper_ballot.pdf"
main_file = "/Users/shannonshao/Desktop/COMP490/Ballots/ESS_paper_ballot2.pdf"

document = open(main_file, 'rb')
#Create resource manager
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
for page in PDFPage.get_pages(document):
    interpreter.process_page(page)
    # receive the LTPage object for the page.
    layout = device.get_result()
    for element in layout:
        if isinstance(element, LTTextBoxHorizontal):
            print(element.get_text())