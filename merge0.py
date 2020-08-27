from os import path, listdir
from PyPDF2 import PdfFileMerger

files_path = path.abspath('') + '/files'

pdfs = [f"{files_path}/{pdf_file}" for pdf_file in listdir(files_path) if pdf_file.endswith('.pdf')]

pdf_merger = PdfFileMerger()

for pdf_file in pdfs:
    pdf_merger.append(open(pdf_file, 'rb'))

with open('final_file.pdf', 'wb') as pdf_final:
    pdf_merger.write(pdf_final)