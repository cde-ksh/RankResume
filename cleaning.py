import ftfy
import re

def clean_text(text):

    # remove extra spaces
    text = re.sub(r' \t+', ' ', text)

    # fixing Uppercase with spaces
    text = re.sub(r'(\b[A-Z])\s+(?=[A-Z]\b)', 'r\1', text)

    # spaces before punchuation
    text = re.sub(r'\s+(,.)', r'\1', text)

    # normalising new lines
    text = re.sub(r'\n+', '\n', text)

    return text.strip()
