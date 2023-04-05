import pdfplumber
from pdfpage import PDFPage



file = "./sample_ballots/Hart_paper_ballot2.pdf"


fp = open(file, 'rb')
pages = PDFPage.get_pages(fp)
sample_ballot = file

report = pdfplumber.open(file).pages[0]
im = report.to_image()

height = 0
num = 0

for page in pages:
  if num >= 1:
      break
  height1 = page.mediabox[1]
  height2 = page.mediabox[3]
  height = abs(height2-height1)
  num += 1

for i, line in enumerate(report.lines):


  print("line found!")
  im.draw_line(((line['x0'], height-line['y0']), (line['x1'], height-line['y1'])), stroke = "green")

im.save("./sample_ballots/lined-paper-pdf.png", format="PNG")
