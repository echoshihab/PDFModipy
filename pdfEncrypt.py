from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog


class PDFEncrypt:
    """Overall class to manage logic for encrypting pdf"""

    def __init__(self):
        self.file_path = ""

    def encrypt_pdf(self, password):
        pdf = PdfFileReader(self.file_path)
        pdf_writer = PdfFileWriter()
        for page in range(pdf.numPages):
            pdf_writer.addPage(pdf.getPage(page))
        pdf_writer.encrypt(password)

        with open("encrpyted_file.pdf", 'wb') as output:
            pdf_writer.write(output)

    def select_pdf(self):
        self.file_path = filedialog.askopenfilename(
            initialdir="/", title="Select a File", filetypes=[("pdf files", "*.pdf")])
