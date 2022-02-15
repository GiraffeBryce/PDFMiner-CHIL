import pdfplumber


#report = pdfplumber.open("C:/Users/aland/Documents/Rice Documents/Rice Freshman Year/PDF Parsing/lswagenergy.pdf").pages[0]
report = pdfplumber.open("/Users/btw4/Desktop/Junior Year/CSCI 390/ESS_paper_ballot.pdf").pages[0]
im = report.to_image()
# im.save("C:/Users/aland/Documents/Rice Documents/Rice Freshman Year/PDF Parsing/", format="PNG")

print(im.draw_lines(report.curves, stroke="red", stroke_width=2))
print(len(report.curves))
#print(report.curves[12])