import sys
sys.path.append('../')

from converter import PDFPageAggregator
from layout import LAParams, LTText, LTTextBox, LTTextLine
from pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfpage import PDFPage
import pdfplumber
import cv2


def is_letter(char):
    if (char.isalpha() == True) or (char.isdigit() == True) or char == "’" or char == "'":
        return True
    else:
        return False

def letter_parse(file, image):

    fp = open(file, 'rb')

    rsrcmgr = PDFResourceManager()
    device = PDFPageAggregator(rsrcmgr, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)

    report = pdfplumber.open(file).pages[0]
    unit = image.shape[1] / report.width


    for page in pages:

        interpreter.process_page(page)
        layout = device.get_result()
        height1 = page.mediabox[1]
        height2 = page.mediabox[3]
        height = abs(height2-height1)
        
        #go through every container
        for lobj in layout:
            #if container is textbox,
            if isinstance(lobj, LTTextBox):
                #go through everything in the textbox.
                for box_obj in lobj:
                    #if in the textbox, there is a textline, go through it.
                    if isinstance(box_obj, LTTextLine):
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
                            if isinstance(char_obj, LTText) and is_letter(char_obj.get_text()):
                                #if this is the first letter in a word, flip the first_char_found flag, concat to string, and record the location of this first letter.
                                if first_char_found == False:
                                    # print("first char found: ", char_obj.get_text())
                                    first_char_found = True
                                    string_word += char_obj.get_text()
                                    xlocation_first_letter = char_obj.bbox[0]
                                    ylocation_first_letter = height - char_obj.bbox[3]
                                    #record the end coordinates of the first letter
                                    xlocation_last_letter = char_obj.bbox[2]
                                    ylocation_last_letter = height - char_obj.bbox[1]
                                else:
                                    string_word += char_obj.get_text()
                                    xlocation_last_letter = char_obj.bbox[2]
                                    ylocation_last_letter = height - char_obj.bbox[1]
                                #if it is not the first letter, and there is a significant space between one letter and the next
                            #if this current character is a word ending character (space, comma, etc add more!), then now we print word and location, and start again.
                            elif (isinstance(char_obj, LTText)):
                                if (first_char_found == True):
                                    # Draw the rects
                                    string_word = ""
                                    first_char_found = False
                                    cv2.rectangle(image, (int(xlocation_first_letter * unit), int(ylocation_first_letter * unit)), (int(xlocation_last_letter * unit), int(ylocation_last_letter * unit)), (0, 0, 255), 2)
        break

    return image
