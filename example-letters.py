import minecart

pdffile = open('/Users/btw4/Desktop/Junior Year/CSCI 390/ESS_paper_ballot.pdf', 'rb')
pdffile1 = open('/Users/btw4/Desktop/Junior Year/CSCI 390/CHIL bubbleballot01.pdf', 'rb')
pdffile2 = open('/Users/btw4/Desktop/Junior Year/CSCI 390/Hart_paper_ballot.pdf', 'rb')
pdffile3 = open('/Users/btw4/Desktop/Junior Year/CSCI 390/Unisyn_paper_ballot.pdf', 'rb')
doc = minecart.Document(pdffile)
page = doc.get_page(0)

for shape in page.shapes.iter_in_bbox((0, 0, 100, 200)):
     print (shape.path, shape.fill.color.as_rgb())
for letter in page.letterings.iter_in_bbox((0, 0, page.width, page.height)):
    im.draw_circle(letter.bbox, 5, fill = (0, 0, 0, 0), stroke=color)
    print (letter)
im = page.images[0].as_pil()  # requires pillow
im.show()