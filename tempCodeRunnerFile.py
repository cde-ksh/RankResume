try:
        doc = fitz.open(file)
        with open("output.txt","a",encoding="utf8") as text:
            for page in doc:
                raw_data = page.get_text("text")
                if raw_data:
                    clean_data = clean_text(raw_data)
                    text.write(clean_data + "\n")