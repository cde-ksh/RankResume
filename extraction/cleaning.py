import ftfy
import re
import unicodedata


def clean_text(text):

    # fixing brokin unicode 
    text = ftfy.fix_text(text)

    # unicode normalisation
    text = unicodedata.normalize("NFKD", text)
    text = text.encode('ascii','ignore').decode()

    # remove extra spaces
    text = re.sub(r'[ \t+]', ' ', text)

    # normalising the spaces
    text = re.sub(r'[^\S\n]+', " ", text).strip()

    # fixing Uppercase with spaces
    text = re.sub(r'(\b[A-Z])\s+(?=[A-Z]\b)', r'\1', text)

    # spaces before punchuation
    text = re.sub(r'\s+([,.;:])', r'\1', text)

    # remove unicode 
    text = re.sub(r'[^a-zA-Z0-9@.+\s,\-:/]', "", text)

    # normalising new lines
    text = re.sub(r'\n+', '\n', text)

    return text.strip()



def find_mail(text):
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)

def find_number(text):
    return re.findall(r'\b[6-9]\d{9}\b', text)
