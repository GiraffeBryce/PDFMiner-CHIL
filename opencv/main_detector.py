import cv2
import pdf2image
import time

from text_detector import letter_parse
from bubble_detector import bubble_parse
from data import data


def parse(fileIndex):

    t0 = time.time()
    
    main_file = "../sample_ballots/" + data[fileIndex]['name'] + ".pdf"

    pages = pdf2image.convert_from_path(main_file)
    for page in pages:
        page.save('temp.png', 'PNG')
        break

    image = cv2.imread('temp.png')
    image = bubble_parse(fileIndex, image)
    image = letter_parse(main_file, image)
    cv2.imwrite("../sample_ballots_output/" + str(fileIndex + 1) + "-" + data[fileIndex]['name'] + '.png', image)

    t1 = time.time()
    print(data[fileIndex]['name'], "processed. Time taken:", str(t1-t0))



def main():
    for fileIndex in range(5):
        parse(fileIndex)

if __name__ == "__main__":
    main()