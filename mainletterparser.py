
# LETTER_PARSE

#IMPORTANT: enter main file name here as a path to a pdf. Include the .pdf ending. It is a string.
#sample path to file: "C:/Users/aland/Documents/Rice Documents/Rice Freshman Year/PDF Parsing/bubbleballot01.pdf"
from converter import PDFPageAggregator
from layout import LAParams, LTComponent, LTCurve, LTImage, LTLine, LTRect, LTText, LTTextBox, LTTextLine
from pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfpage import PDFPage
import pdfplumber

file1 = "/Users/btw4/Desktop/Junior Year/CSCI 390/new ballots/baker.pdf"
file2 = "/Users/btw4/Desktop/Junior Year/CSCI 390/new ballots/broward.pdf"
file3 = "/Users/btw4/Desktop/Junior Year/CSCI 390/new ballots/flagler.pdf"
file4 = "/Users/btw4/Desktop/Junior Year/CSCI 390/new ballots/dekalb.pdf"
file5 = "/Users/btw4/Desktop/Junior Year/CSCI 390/new ballots/mississippi.pdf"
file6 = "/Users/btw4/Desktop/Junior Year/CSCI 390/new ballots/bexar.pdf"
file7 = "/Users/btw4/Desktop/Junior Year/CSCI 390/new ballots/altona.pdf"

def is_letter(char):
    if (char.isalpha() == True) or (char.isdigit() == True) or char == "’" or char == "'":
        return True
    else:
        return False

def letter_parse(file, threshold, image, bubble_found):

    main_file = file

    main_threshold = threshold

    #Main Code for PDFMINER TEXT LOCATION. GO TO LINE 97 for CURVE DETECTION


    fp = open(main_file, 'rb')

    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)

    sample_ballot = main_file

    # Choosing page of ballot to run the code. Input different index for diff pages.
    report = pdfplumber.open(sample_ballot).pages[0]
    # Create the image to save
    im = image
    num = 0

    for page in pages:
        if num >= 1:
            break
        print('Processing next page...')
        interpreter.process_page(page)
        layout = device.get_result()
        height1 = page.mediabox[1]
        height2 = page.mediabox[3]
        height = abs(height2-height1)
        num += 1
        xlocation_last_prev = 0
        center = (0,0)
        center_prev = (0,0)
        
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
                        #first_stop = True
                        possible_bubble_right = False
                        #go through all the characters inthe textline.
                        for char_obj in box_obj:
                            center_prev = center
                            possible_bubble_left = possible_bubble_right
                            possible_bubble_right = False
                            #if we haven't found the first character in whatever word, initialize variables to start (or start over)
                            if first_char_found == False:
                                string_word = ""
                                xlocation_first_letter = None
                                ylocation_first_letter = None
                            #after checking first_char_found flag, now check if this current char is a letter and not a word ending char
                            if isinstance(char_obj, LTText) and (is_letter(char_obj.get_text()) == True):
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
                                    ylocation_average = ((ylocation_first_letter) + (height - char_obj.bbox[1])) / 2
                                    xlocation_average = (xlocation_first_letter + xlocation_last_letter) / 2
                                    center = (xlocation_average, ylocation_average)
                                else:
                                    string_word += char_obj.get_text()
                                    xlocation_last_letter = char_obj.bbox[2]
                                    ylocation_last_letter = height - char_obj.bbox[1]
                                    ylocation_average = ((ylocation_first_letter) + (height - char_obj.bbox[1])) / 2
                                    xlocation_average = (xlocation_first_letter + xlocation_last_letter) / 2
                                    center = (xlocation_average, ylocation_average)
                                #if it is not the first letter, but there is not a significant space between one letter and the next
                                if (not (abs(char_obj.bbox[0]-xlocation_last_prev) < main_threshold)) and not bubble_found:
                                #or else, this is just a letter in the middle of the word. So just concat to string.
                                    print("bubble before ", string_word)
                                    possible_bubble_right = True
                                    #print("Space ", abs(char_obj.bbox[0]-xlocation_last_prev), " before ", string_word, "too big")
                                    # xlocation_last_letter = char_obj.bbox[2]
                                    # ylocation_last_letter = height - char_obj.bbox[1]
                                    center2 = (xlocation_last_letter, ylocation_average)
                                    im.draw_circle(center2, 5, fill = (0, 0, 0, 0), stroke="green")
                                    # print("space ", abs(char_obj.bbox[0]-xlocation_last_prev), " before ", string_word, " small enough")
                                #if it is not the first letter, and there is a significant space between one letter and the next
                                xlocation_last_prev = xlocation_last_letter
                            #if this current character is a word ending character (space, comma, etc add more!), then now we print word and location, and start again.
                            elif (isinstance(char_obj, LTText)): # and (first_char_found == True): #and len(string_word) == 1:
                                possible_bubble_right = True
                                # if (possible_bubble_left and len(string_word) == 1):
                                #     print("one")
                                if (first_char_found == True):
                                    # circling the bubbles, heuristic being the word is a single letter that is circular and far enough away from the words next to it
                                    if (possible_bubble_left and possible_bubble_right and (len(string_word) == 1) and not (string_word.__eq__('r')) and not (string_word.__eq__('I')) and not (string_word.__eq__('1')) and not (string_word.__eq__('T'))):
                                        print("one")
                                        im.draw_circle(center_prev, 5, fill = (0, 0, 0, 0), stroke="blue")
                                    # Comment out to see the lines
                                    # im.draw_line(((xlocation_first_letter, ylocation_first_letter), (xlocation_last_letter, ylocation_last_letter)), stroke="brown")
                                    # Comment out to see the rects
                                    im.draw_rect((xlocation_first_letter, ylocation_first_letter, xlocation_last_letter, ylocation_last_letter))
                                    string_word = ""
                                    first_char_found = False

    #im.save("/Users/btw4/Desktop/Junior Year/CSCI 390/new ballots/letter altona28.png", format="PNG")
    return im
