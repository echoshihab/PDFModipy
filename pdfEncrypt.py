from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import *
from tkinter import filedialog


class PDFEncrypt:
    """Overall class to manage UI & Logic for encrypting pdf"""

    def __init__(self, UI):
        self.file_path = ""

        # buttons
        self.select_btn = Button(
            UI.encrypt_tab, text="Select File", command=self._get_file_path)
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

    def _encrypt_pdf(self, password):
        pdf = PdfFileReader(self.file_path)
        pdf_writer = PdfFileWriter()
        for page in range(pdf.numPages):
            pdf_writer.addPage(pdf.getPage(page))
        pdf_writer.encrypt(password)

        with open("encrpyted_file.pdf", 'wb') as output:
            pdf_writer.write(output)

    def _is_valid_password(self):
        password = self.encrypt_password.get()
        confirm_password = self.confirm_password.get()
        if(password == confirm_password):
            return True
        return False

    # refactor disply info and danger text+ add validations to _is_valid_password() method

    def complete_encrypt_tasks(self):
        password = self._is_valid_password()
        if(password):
            self._encrypt_pdf(self.encrypt_password.get())
            self._display_info_text()
            return True
        else:
            self._display_error_text()

    def _display_info_text(self):
        self.info_text.grid(row=6, column=3)
        self.info_text.configure(
            text="Task Complete!", foreground="green")

    def _display_error_text(self):
        self.info_text.grid(row=6, column=3)
        self.info_text.configure(
            text="Passwords must match", foreground="red")

    def select_pdf(self):
        self.file_path = filedialog.askopenfilename(
            initialdir="/", title="Select a File", filetypes=[("pdf files", "*.pdf")])

    def _get_file_path(self):
        self.select_pdf()
        self.file_path_label.configure(
            text=self._shorten_file_name())
        self.file_path_label.grid(row=0, column=1)

    def _shorten_file_name(self):
        file_name = self.file_path.split('/')[-1]
        return file_name if len(file_name) < 36 else file_name[:36] + "..."

    def display_UI(self):
        self.select_btn.grid(row=0, column=0)
        self.encrypt_password_label.grid(
            row=2, column=0, sticky='E')
        self.encrypt_password.grid(row=2, column=1, sticky='W')
        self.confirm_password_label.grid(
            row=3, column=0, sticky='E')
        self.confirm_password.grid(row=3, column=1, sticky='W')
        self.encrypt_btn.grid(row=4, column=0)
