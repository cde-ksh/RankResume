
with open("output.txt", "r", encoding="utf8") as f:
    text = f.read()

def link_extractor(text):
    lines = text.splitlines()
    link = []

    for line in lines:
        line = line.strip()
        if line.startswith("[LINK]"):
            link.append(line)
    return "\n".join(link)

with open("link.txt", "w", encoding="utf8") as f:
    f.write(str(link_extractor(text)))