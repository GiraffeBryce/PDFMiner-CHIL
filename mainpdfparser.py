import pdfplumber
from layout import LAParams, LTTextBox, LTChar,  LTTextLine, LTText, LTImage, LTCurve, LTFigure, LTRect, LTAnno
from pdfpage import PDFPage
from pdfinterp import PDFResourceManager
from pdfinterp import PDFPageInterpreter
from converter import PDFPageAggregator

#PDFPlumber
import numpy as np




#helper function
def is_letter(char):
    if (char.isalpha() == True) or (char.isdigit() == True) or char == "’" or char == "'":
        return True
    else:
        return False


#IMPORTANT: enter main file name here as a path to a pdf. Include the .pdf ending. It is a string.
#sample path to file: "C:/Users/aland/Documents/Rice Documents/Rice Freshman Year/PDF Parsing/bubbleballot01.pdf"
main_file = "/Users/btw4/Desktop/Junior Year/CSCI 390/Unisyn_paper_ballot.pdf"





#Main Code for PDFMINER TEXT LOCATION. GO TO LINE 97 for CURVE DETECTION


fp = open(main_file, 'rb')
# fp = open("C:/Users/aland/Documents/Rice Documents/Rice Freshman Year/PDF Parsing/ESS_paper_ballot.pdf", 'rb')
# fp = open("C:/Users/aland/Documents/Rice Documents/Rice Freshman Year/PDF Parsing/Hart_paper_ballot.pdf", 'rb')

rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
pages = PDFPage.get_pages(fp)

for page in pages:
    print('Processing next page...')
    interpreter.process_page(page)
    layout = device.get_result()
    
    #go through every container
    for lobj in layout:
        #if container is textbox,
        if isinstance(lobj, LTTextBox):
            """ x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
            print('At %r is text: %s' % ((x, y), text)) """
            #go through everything in the textbox.
            for box_obj in lobj:
                #if in the textbox, there is a textline, go through it.
                if isinstance(box_obj, LTTextLine):
                    """ x, y, text = box_obj.bbox[0], box_obj.bbox[3], box_obj.get_text()
                    print('At %r is text: %s' % ((x, y), text)) """
                    #print(box_obj.get_text)
                    #preliminary flag to start process of finding a singular word
                    first_char_found = False
                    #go through all the characters inthe textline.
                    for char_obj in box_obj:
                        #if we haven't found the first character in whatever word, initialize variables to start (or start over)
                        if first_char_found == False:
                            string_word = ""
                            xlocation_first_letter = None
                            ylocation_first_letter = None
                        #after checking first_char_found flag, now check if this current char is a letter and not a word ending char
                        if isinstance(char_obj, LTText) and (is_letter(char_obj.get_text()) == True):
                            #if this is the first letter in a word, flip the first_char_found flag, concat to string, and record the location of this first letter.
                            if first_char_found == False:
                                first_char_found = True
                                string_word += char_obj.get_text()
                                xlocation_first_letter = char_obj.bbox[0]
                                ylocation_first_letter = char_obj.bbox[3]
                                xlocation_last_letter = char_obj.bbox[0]
                                ylocation_last_letter = char_obj.bbox[3]
                            #or else, this is just a letter in the middle of the word. So just concat to string.
                            else:
                                string_word += char_obj.get_text()
                                xlocation_last_letter = char_obj.bbox[0]
                                ylocation_last_letter = char_obj.bbox[3]
                        #if this current character is a word ending character (space, comma, etc add more!), then now we print word and location, and start again.
                        # elif first_char_found == True and is_word_ending_char(char_obj.get_text()):
                        elif (isinstance(char_obj, LTText)) and (first_char_found == True):
                            #print("%r is the first letter in %s, %r is the last letter" % (xlocation_first_letter, string_word, xlocation_last_letter))
                            xlocation_average = (xlocation_first_letter + xlocation_last_letter) / 2
                            ylocation_average = (ylocation_first_letter + ylocation_last_letter) / 2
                            print("At %r is the word: %s" % ((xlocation_average, ylocation_average), string_word))
                            first_char_found = False





#PDFPLUMBER CURVE DETECTION
# Loading the file
# sample_ballot = "/Users/arianawang/Documents/Rice/Sample/CHIL bubbleballot01 (1).pdf"

sample_ballot = main_file

# Choosing page of ballot to run the code. Input different index for diff pages.
report = pdfplumber.open(sample_ballot).pages[0]
# Create the image to save
im = report.to_image()

# Colors that the coordinates will be mapped in
colors = [ "gray", "red", "blue", "green" ]

# Iterate through the detected curves
for i, curve in enumerate(report.curves):
    # If the curve detected is not a line (i.e. two points on the curve detected)
    if len(curve["points"]) != 2:
        print ("curve found!")
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
#im.save("/Users/btw4/Desktop/Junior Year/CSCI 390/ess test.png", format="PNG")

# Github link: https://github.com/jsvine/pdfplumber/blob/stable/examples/notebooks/ag-energy-roundup-curves.ipynb

    