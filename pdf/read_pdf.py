from PyPDF2 import PdfFileReader

pdf_document = "C:\\Out_file\\card_0355.pdf"
with open(pdf_document, "rb") as filehandle:
    pdf = PdfFileReader(filehandle)
    info = pdf.getDocumentInfo()
    pages = pdf.getNumPages()
    print(info)
    print("Number of pages:", pages)
    for item in range(pages):
        page = pdf.getPage(item)
        print(page)
        text = page.extractText()
        list = text.split(",")
        print(text)



