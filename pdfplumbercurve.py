import pdfplumber


#report = pdfplumber.open("C:/Users/aland/Documents/Rice Documents/Rice Freshman Year/PDF Parsing/lswagenergy.pdf").pages[0]
report = pdfplumber.open("C:/Users/aland/Documents/Rice Documents/Rice Freshman Year/PDF Parsing/bubbleballot01.pdf").pages[0]
im = report.to_image()
im
print(len(report.curves))
print(report.curves[12])