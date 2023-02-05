import pdfplumber
from mainletterparser import letter_parse

from mainpdfparser import curve_parse

from mainshapeparser import rect_parse, image_parse, line_parse

def parse(filename):
    
    main_file = "./sample_ballots/" + filename + ".pdf"

    # threshold = 35 # original
    threshold = 60
    bubble_found = False

    im, bubble_found = curve_parse(main_file)

    print("curve parsed, bubble found? ", bubble_found)

    im, bubble_found = rect_parse(main_file, im, bubble_found)

    im = letter_parse(main_file, threshold, im, bubble_found)

    print("letters parsed")

    im.save("./sample_ballots_output/" + filename + "output.png", format="PNG")

def main():
    #Input file name (remove .pdf)
    parse("ESS_paper_ballot")

if __name__ == "__main__":
    main()