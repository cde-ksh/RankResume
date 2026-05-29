from extraction.extractor import extract_text
from extraction.cleaning import clean_text

SECTION_ALIASES = {

    # =========================
    # PROFILE / SUMMARY
    # =========================
    "summary": [
        "summary",
        "professional summary",
        "career summary",
        "executive summary",
        "profile",
        "professional profile",
        "about me",
        "about",
        "overview",
        "career objective",
        "objective",
        "personal statement"
    ],

    # =========================
    # CONTACT INFORMATION
    # =========================
    "contact": [
        "contact",
        "contact information",
        "personal details",
        "personal information",
        "details"
    ],

    # =========================
    # SKILLS
    # =========================
    "skills": [
        "skills",
        "technical skills",
        "technical proficiencies",
        "core competencies",
        "competencies",
        "expertise",
        "key skills",
        "areas of expertise",
        "technical expertise",
        "skill set",
        "professional skills",
        "technologies",
        "tools & technologies",
        "tech stack",
        "stack",
        "programming skills"
    ],

    # =========================
    # PROGRAMMING
    # =========================
    "programming": [
        "programming",
        "programming languages",
        "languages",
        "coding languages"
    ],

    # =========================
    # FRAMEWORKS
    # =========================
    "frameworks": [
        "frameworks",
        "libraries",
        "frameworks & libraries",
        "frontend frameworks",
        "backend frameworks"
    ],

    # =========================
    # DATABASES
    # =========================
    "databases": [
        "databases",
        "database",
        "database technologies",
        "dbms"
    ],

    # =========================
    # TOOLS
    # =========================
    "tools": [
        "tools",
        "developer tools",
        "software tools",
        "platforms"
    ],

    # =========================
    # EDUCATION
    # =========================
    "education": [
        "education",
        "academic background",
        "academic qualifications",
        "educational qualifications",
        "qualifications",
        "education details",
        "academic details"
    ],

    # =========================
    # EXPERIENCE
    # =========================
    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "career history",
        "work history",
        "industry experience",
        "professional background"
    ],

    # =========================
    # PROJECTS
    # =========================
    "projects": [
        "projects",
        "project",
        "key projects",
        "personal projects",
        "academic projects",
        "professional projects",
        "major projects",
        "relevant projects",
        "project experience"
    ],

    # =========================
    # INTERNSHIPS
    # =========================
    "internships": [
        "internships",
        "internship",
        "training",
        "industrial training",
        "summer training",
        "apprenticeship"
    ],

    # =========================
    # CERTIFICATIONS
    # =========================
    "certifications": [
        "certifications",
        "certification",
        "licenses",
        "license",
        "courses",
        "online courses",
        "credentials"
    ],

    # =========================
    # ACHIEVEMENTS
    # =========================
    "achievements": [
        "achievements",
        "achievement",
        "awards",
        "honors",
        "accomplishments",
        "recognitions"
    ],

    # =========================
    # RESEARCH / PUBLICATIONS
    # =========================
    "research": [
        "research",
        "research papers",
        "publications",
        "published work",
        "papers",
        "journals"
    ],

    # =========================
    # VOLUNTEER
    # =========================
    "volunteer": [
        "volunteer experience",
        "volunteering",
        "community service",
        "social work"
    ],

    # =========================
    # ACTIVITIES
    # =========================
    "activities": [
        "extracurricular activities",
        "activities",
        "co-curricular activities"
    ],

    # =========================
    # LANGUAGES
    # =========================
    "languages": [
        "languages",
        "spoken languages"
    ],

    # =========================
    # INTERESTS
    # =========================
    "interests": [
        "interests",
        "hobbies",
        "personal interests"
    ],

    # =========================
    # REFERENCES
    # =========================
    "references": [
        "references",
        "reference"
    ]
}

def section_seperator(file_path=""):
    with open("output.txt", "r",encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            cleaned_line = clean_text(line)
            if cleaned_line in SECTION_ALIASES:
                print(line.strip())


def section_extractor(file_path=""):
    current_section = None
    parsed_sections = {}
    with open("output.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

        for line in lines:
            cleaned_line = clean_text(line)

            if cleaned_line in SECTION_ALIASES:
                current_section = cleaned_line
                parsed_sections[current_section] = []

            else:
                if current_section:
                    parsed_sections[current_section].append(line.strip())

        
    with open("seperator.txt","w", encoding="utf8") as f:
        for section, content in parsed_sections.items():
            f.write(f"{section.upper()}\n")
            
            for line in content:
                f.write(f"{line}\n")
            
            f.write("\n")

    return parsed_sections

print(section_extractor())