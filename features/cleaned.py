import spacy
from spacy.matcher import PhraseMatcher

# spacy
nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
doc = nlp("Hello i am kira and i am making a python project")
print(doc)

