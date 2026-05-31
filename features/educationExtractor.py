import spacy
from spacy.matcher import PhraseMatcher
from spacy.pipeline import EntityRuler
from extraction.extractor import extract_text

# spacy
nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

with open("seperator.txt", "r", encoding="utf8") as f:
    text = f.read()

def education_extractor(text):
    lines = text.splitlines()
    education = []        
    collect = False
    
    for line in lines:
        line = line.strip()
        if line.lower() == "education":
            collect = True
            continue
        if collect and line.isupper():
            break
        if collect:
            education.append(line)
    return "\n".join(education)

with open("education.txt", "w", encoding="utf8") as f:
    f.write(str(education_extractor(text)))
