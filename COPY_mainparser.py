import pdfplumber
from COPY_mainletterparser import letter_parse

from COPY_mainpdfparser import curve_parse

from COPY_mainshapeparser import rect_parse, image_parse, line_parse

def parse(filename):
    
    main_file = "./sample_ballots/" + filename + ".pdf"

    # threshold = 35 # original
    threshold = 60
    bubble_found = False

    im, letterLocation = letter_parse(main_file, threshold, bubble_found)

    print("letters parsed")

    im, bubble_found = curve_parse(main_file, im, letterLocation)

    print("curve parsed, bubble found? ", bubble_found)

    im, bubble_found = rect_parse(main_file, im, bubble_found)

    im.save("./sample_ballots_output/COPY_" + filename + "output.png", format="PNG")

def main():
    #Input file name (remove .pdf)
    parse("ESS_paper_ballot")

if __name__ == "__main__":
    main()