import spacy
from spacy.matcher import PhraseMatcher
from extraction.extractor import extract_text

# spacy
nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")


file = "/Users/kshiraj/Downloads/resumes2/ResumeABHINAYAP.pdf"


# <----- loading skill taxonomy ----->
def load_skill_taxonomy(file_path = "skillTaxonomy.py"):
    with open(file_path, 'r', encoding='utf8') as f:
        lines = f.readlines()
        skills = []
        for line in lines:
            skills.append(line.strip())
        return skills

skills = load_skill_taxonomy()
patterns = [nlp.make_doc(skill) for skill in skills]
matcher.add("SKILLS", patterns)



# <----- extracting skills ----->
def extract_skills(text):
    text = extract_text(file)
    doc = nlp(text)

    matches = matcher(doc)

    found_skills = set()
    for _, start, end in matches:
        skill = doc[start:end].text.lower()
        found_skills.add(skill)

    return list(found_skills)
    

