from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import *
from tkinter import filedialog


class PDFSplitter:
    """Overall class to manage logic and UI for splitting pdf"""

    def __init__(self, UI):
        self.file_path = ""

        # buttons
        self.select_btn = Button(
            UI.split_tab, text="Select File", command=self._get_file_path)
        self.split_btn = Button(UI.split_tab, text="Split")

        # labels
        self.file_path_label = Label(UI.split_tab)
        self.end_page_label = Label(UI.split_tab, text="End Page")
        self.start_page_label = Label(UI.split_tab, text="Start Page")
        self.info_text = Label(UI.split_tab, text="working...")

        # input fields
        self.start_page = Entry(UI.split_tab, width=10)
        self.end_page = Entry(UI.split_tab, width=10)

    def _split_pdf(self, start_page, end_page):
        pdf = PdfFileReader(self.file_path)
        pdf_writer = PdfFileWriter()
        for page in range(start_page-1, end_page):
            pdf_writer.addPage(pdf.getPage(page))

        with open("outFile.pdf", 'wb') as output:
            pdf_writer.write(output)

    def select_pdf(self):
        self.file_path = filedialog.askopenfilename(
            initialdir="/", title="Select a File", filetypes=[("pdf files", "*.pdf")])

    def display_UI(self):
        self.select_btn.grid(row=0, column=0)
        self.start_page_label.grid(row=3, sticky='W')
        self.start_page.grid(row=3, column=1, sticky='W')
        self.end_page_label.grid(row=4, sticky='W')
        self.end_page.grid(row=4, column=1, sticky='W')
        self.split_btn.grid(row=5, column=0)

    def _shorten_file_name(self):
        file_name = self.file_path.split('/')[-1]
        return file_name if len(file_name) < 36 else file_name[:36] + "..."

    def _get_file_path(self):
        """gets file path of pdf for splitting"""
        self.select_pdf()
        self.file_path_label.configure(
            text=self._shorten_file_name())
        self.file_path_label.grid(row=0, column=1)

    def complete_split_tasks(self):
        """completes split pdf related tasks """
        self._split_pdf(
            int(self.start_page.get()), int(self.end_page.get()))  # need to validate input here
        self._clean_up_page_entry()
        self._display_info_texts()

    def _display_info_texts(self):
        self.info_text.grid(row=6, column=3)
        self.info_text.configure(
            text="Task Complete!", foreground="green")

    def _clean_up_page_entry(self):
        """blanks out start and end page text boxes"""
        self.start_page.delete(0, "end")
        self.end_page.delete(0, "end")
