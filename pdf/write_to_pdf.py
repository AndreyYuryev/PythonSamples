from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Welcome!", ln=1, align="C")
pdf.output("C:\\Out_file\\simple.pdf")
