from pdfminer.layout import LAParams, LTTextBox, LTChar,  LTTextLine, LTText, LTImage, LTCurve, LTFigure, LTRect, LTAnno
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

#fp = open("C:/Users/aland/Documents/Rice Documents/Rice Freshman Year/PDF Parsing/bubbleballot01.pdf", 'rb')
fp = open("C:/Users/aland/Documents/Rice Documents/Rice Freshman Year/PDF Parsing/bubbleballot01.pdf", 'rb')
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
                        #after checking first_char_found flag, now check if this current char is a letter.
                        if isinstance(char_obj, LTChar) and (char_obj.get_text() != " ") and (char_obj.get_text() != ",") and (char_obj.get_text() != "(") and (char_obj.get_text() != ")b"):
                            #if this is the first letter in a word, flip the first_char_found flag, concat to string, and record the location of this first letter.
                            if first_char_found == False:
                                first_char_found = True
                                string_word += char_obj.get_text()
                                xlocation_first_letter = char_obj.bbox[0]
                                ylocation_first_letter = char_obj.bbox[3]
                            #or else, this is just a letter in the middle of the word. So just concat to string.
                            else:
                                string_word += char_obj.get_text()
                        #if this current character is a word ending character (space, comma, etc add more!), then now we print word and location, and start again.
                        elif first_char_found == True and (char_obj.get_text() == " " or char_obj.get_text() == ","):
                            print("At %r is the word: %s" % ((xlocation_first_letter, ylocation_first_letter), string_word))
                            first_char_found = False


                            
                            
""" concatenated_string = ""
for char in list_of_chars:
    concatenated_string += char
print(concatenated_string) """


'''

initialize word string
first_char_found = false
when first char is found, concat. it to the string and save the bbox of it. 
first_char_found = true. 
keep going through all chars until a diff symbol is found (a space, a comma, anything not a char)
    when a diff symbol is found, the word has ended. print out the word,
    and the bbox of the first letter in the word.
    first_char_found = false
start over again.
'''
                            

""" if isinstance(lobj, LTTextBox):
            x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
            print('At %r is text: %s' % ((x, y), text)) """


    