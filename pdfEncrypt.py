from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import *
from tkinter import filedialog


class PDFEncrypt:
    """Overall class to manage UI & Logic for encrypting pdf"""

    def __init__(self, UI):
        self.file_path = ""

        # buttons
        self.select_btn = Button(UI.encrypt_tab, text="Select File")
        self.encrypt_btn = Button(UI.encrypt_tab, text="Encrypt")

        # labels
        self.file_path_label = Label(UI.encrypt_tab)
        self.encrypt_password_label = Label(UI.encrypt_tab,  text="Password")
        self.confirm_password_label = Label(
            UI.encrypt_tab, text="Confirm Password")
        self.info_text = Label(UI.encrypt_tab, text="working...")

        # Input fields
        self.encrypt_password = Entry(UI.encrypt_tab, show="*", width=10)
        self.confirm_password = Entry(UI.encrypt_tab, show="*", width=10)

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
