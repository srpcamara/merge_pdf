from os import path, listdir
from PyPDF2 import PdfFileMerger
from datetime import date

files_path = path.abspath('') + '/files'
data = date.today()

arquivos = [
    ("nu", "Cartão Nubank")
    ,("digio", "Cartão Digio")
    ,("cic", "CIC - Condomínio")
    ,("crsl", "CRSL - Condomínio")
    ,("tim", "TIM")
]

for arquivo in arquivos:

    pdf_merger = PdfFileMerger()

    boleto = f"{files_path}/{arquivo[0]}.pdf" 
    comprovante = f"{files_path}/{arquivo[0]}_comp.pdf" 
    arquivo_final = f"{files_path}/{arquivo[1]} {data.year}.{'{:02d}'.format(data.month)}.pdf"   

    if path.isfile(boleto): 
        
        pdf_merger.append(open(boleto, 'rb'))
        pdf_merger.append(open(comprovante, 'rb'))

        with open(arquivo_final, 'wb') as pdf_final:
            pdf_merger.write(pdf_final)
        
        pdf_merger.close()
           