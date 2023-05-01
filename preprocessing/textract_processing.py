import textract
import re

def get_content_as_string(filename):
    text = textract.process(filename)
    lower_case_string =  str(text.decode('utf-8')).lower()
    return lower_case_string