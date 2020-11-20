from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog


class PDFWorker:
    def __init__(self):
        self.file_path = ""

    def split_pdf(self, start_page, end_page):
        pdf = PdfFileReader(self.file_path)
        pdf_writer = PdfFileWriter()
        for page in range(start_page-1, end_page):
            pdf_writer.addPage(pdf.getPage(page))

        with open("outFile.pdf", 'wb') as output:
            pdf_writer.write(output)

    def merge_pdf(self):
        print("merge")

    def encrypt_pdf(self):
        print("encrypt")

    def select_pdf(self):
        self.file_path = filedialog.askopenfilename(
            initialdir="/", title="Select a File", filetypes=[("pdf files", "*.pdf")])
