import pdfplumber

from COPY_mainletterparser import letter_parse
from COPY_mainparser import parse
from COPY_mainpdfparser import curve_parse
from COPY_mainshapeparser import rect_parse, image_parse, line_parse

parse("CHIL bubbleballot01")
parse("ClearBallot_paper_ballot")
parse("ClearBallot_paper_ballot2")
parse("ESS_paper_ballot")
parse("ESS_paper_ballot2")
parse("Hart_paper_ballot")
parse("Hart_paper_ballot2")
parse("Unisyn_paper_ballot")
parse("Unisyn_paper_ballot2")
parse("sample_ballot")
