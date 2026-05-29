def skill_seperator(file_path=""):
    with open("output.txt", "r",encoding="utf8") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip().lower() in sections:
                print(line)
