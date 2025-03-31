import fitz

with fitz.open("files/students.pdf") as file:
    for page in file:
        print(page.get_text())