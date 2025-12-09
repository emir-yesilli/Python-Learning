from pdf2docx import Converter

pdfFile = "Materials/example.pdf"
docxFile = "Materials/docx.docx"

cv = Converter(pdfFile)
cv.convert(docxFile)
cv.close()
