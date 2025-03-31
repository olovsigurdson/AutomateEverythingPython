from fpdf import FPDF


pdf = FPDF(orientation="P", unit='pt', format='A4')
pdf.add_page()

pdf.image('files/STREETFIGHTER.png', w=200, h=190)
pdf.set_font(family="Arial", style="B", size=24)
pdf.cell(w=0, h=40, txt="Nämen hej!!!", align="C", border=0, ln=1)

pdf.set_font(family="Arial", style="B", size=12)
pdf.multi_cell(w=0, h=20, txt="""
Här är en cell Med två rader
""", align="C", border=0)

pdf.output('files/pdf_streetfighter.pdf')


