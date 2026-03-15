import os
import fitz
import pdfplumber
from docx import Document
import pypandoc

# getting the extension type of the file

file = "/Users/kshiraj/Downloads/deterministic-resume-intelligence-main 2/data/sample/10089434.pdf"
ext = os.path.splitext(file)[1].lower()

# extracting text from pdf files 

if ext == '.pdf':
    with pdfplumber.open(file) as pdf:

        with open("output.txt","w",encoding="utf8") as text:
             
            for page in pdf.pages:
                content = page.extract_text()   

                if content:
                    text.write(content)
                tables = page.extract_tables()

                for table in tables:
                    for row in table:
                        row_text = " | ".join(str(cell) for cell in row if cell)
                        text.write(row_text + "\n")
                
                     
# extracting data from a docx file

if ext == '.docx':
    doc = Document(file)

    with open("output.txt","w", encoding="utf8") as f:
        for para in doc.paragraphs:
            f.write(para.text + "\n")

        for table in doc.tables:
            for row in table.rows:
                row_text = " | ".join(cell.text for cell in row.cells)
                f.write(row_text + "\n")


# extracting files from a doc file

if ext == '.doc':
    doc_file = file + "x"
    
    pypandoc.convert_file(file,"docx",outputfile=doc_file)

    doc = Document(doc_file)

    with open("output.txt","w", encoding="utf8") as f:
        for para in doc.paragraphs:
            f.write(para.text + "\n")

        for table in doc.tables:
            for row in table.rows:
                row_text = " | ".join(cell.text for cell in row.cells)
                f.write(row_text + "\n")


# reading the extracted text from the 

print("\n <--- Extracted text: ---> \n")

with open("output.txt","r") as f:
    data = f.readlines()
    for line in data:
        print(line)
print("\n <--- Extraction Ended ---> \n")