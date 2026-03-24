from cleaning import find_number, find_mail

sections = {
    "skills": ["skills", "technical skills"],
    "experience": ["experience"],
    "education": ["education"],
    "certifications": ["certifications"],
    "projects": ["projects"],
}

def clean_line(line):
    return line.strip().lower()


current_sections = None

result = {"skills": [],
          "experience": [],
          "education": [],
          "certifications": [],
          "projects": [],
        }


with open ("output.txt","r") as f:
    data = f.readlines()
    for line in data:
        cleaned = clean_line(line)

        found_section = None
        for section, keywords in sections.items():
            if cleaned in keywords:
                found_section = section
                break


        if found_section:
            current_sections = found_section
            print(current_sections)

        elif current_sections:
            result[current_sections].append(line.strip())



open("seperator.txt", "w").close()

with open("seperator.txt", "a", encoding="utf8") as f:
    for section, item in result.items():
       f.write(section.upper()+"\n\n")
       f.write("\n".join(item)+"\n\n")

f.close()


# Phone-Number finding
all_mails = []
all_numbers  = []

with open("output.txt", "r", encoding="utf8") as f:
    for line in f:
        nums = find_number(line)
        email = find_mail(line)

        if nums:
            all_numbers.extend(nums)
            all_mails.extend(email)

mails = set(all_mails)
numbers = set(all_numbers)


with open("seperator.txt", "a", encoding="utf8") as f:
    for num in numbers:
        f.write("<--- Contact Information --->" + "\n")
        f.write("Phone Number: " + num + "\n")
    for email in mails:
        f.write("Email: " + email + "\n")

