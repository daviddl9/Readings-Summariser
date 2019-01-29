from gensim.summarization import summarize
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from six import StringIO

FILE_PATH = '/Users/David/PycharmProjects/summary/Week 2- Multiculturalism in Singapore.pdf'
PAGE_RANGE = [1, 18]
SUMMARY_RATIO = 0.7
SUMMARY_LENGTH = 500 # length of summary in words
SUMMARY_FILE_NAME = 'summary.txt'

def convert(fname, pages=None):

    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    return text


# Change page range and file name where necessary
read_text = convert(FILE_PATH, PAGE_RANGE)
read_text = read_text.replace('\n', '') # Remove newline characters to clean up the pdf text.
f = open(SUMMARY_FILE_NAME, 'w+') # File where summary is written to
f.write(summarize(read_text, SUMMARY_RATIO, SUMMARY_LENGTH)) # Change the 500 to the number of words required in the summary
f.close()
