'''
    Get Words Databases
    cleaning PDF with words extracted
    1. ([^ \w.]{0,1}\d{1,4} [\wa-zA-Z\u00C0-\u017F,;' ]+ [\wa-zA-Z\u00C0-\u017F,; \(\)]+) -> \n$1
    2. Delete pattern (\d+ \| \d+)
    3. (\* [a-zA-Z\u00C0-\u017F ,'-\.\?\d!:;%«»]+) in progress page 2562 found 4989 of 4904?
    3.1. (\* [a-zA-Z\u00C0-\u017F ,'-\.\?\d!:;%«»]+\n?[a-zA-Z\u00C0-\u017F ,'-\.\?\d!:;%«»]+)
    
    wildcard for lookin up: ^[^\d\W]
'''
from ast import pattern
from PyPDF2 import PdfReader
import re


pdf = PdfReader('french_frequancy_words.pdf')
number_of_pages = len(pdf.pages)
page = pdf.pages[17]
print(page.extract_text())
#pattern_sub = r"(\n\d+ \| \d+[\+\- lns]+\n\d{1})|(\n\d+ \| \d+\+n\n\d{1})|(\n\d+ \| \d+\n\d{1})|(\n\d+ \| \d+\+s\n\d{1})|(\d+ \| \d+\n\d{1})"

with open('pdf.txt', 'w', encoding='utf-8') as file:
    for i in range(17,477):
        print(f"Writing page {i}")
        page = pdf.pages[i]
        text = page.extract_text()
        #text = re.sub(pattern_sub, " \n", text, flags=re.MULTILINE)
        file.write(text)
        


with open('clean_pdf.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Busca coincidencias utilizando la expresión regular
matches = re.findall(r"(^\d+ [\w ,;\(\)]+$)|(^\* [\w, '-]+)", content, re.MULTILINE)
matches_2 = re.findall(r"^\d+ [\w ,;\(\)]+\n^\* [\w, '-]+", content, re.MULTILINE)
# Imprime las coincidencias
print(len(matches))


print("\n\n"+"-"*20+"\n\n")

print(len(matches_2))
with open("matches.txt", "w") as texto:
    for index, match in enumerate(matches_2):
        print(f"index: {index}")
        print(match)
        print(repr(str(match).split(" ")[0]))
        print("\n")
        texto.write(match)

