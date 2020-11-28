from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import *
from tkinter import filedialog


class PDFMerger:
    """Overall class to manage pdf merge and related UI"""

    def __init__(self, UI):
        self.file_paths = []

        self.merge_btn = Button(UI.merge_tab, text="Merge")

        self.select_btn = Button(
            UI.merge_tab, text="Select File", command=self._get_file_paths)

        # labels
        self.file_path_label = Label(UI.merge_tab)
        self.info_text = Label(UI.merge_tab, text="working...")

    def select_pdfs(self):
        self.file_paths = filedialog.askopenfilenames(
            initialdir="/", title="Select Files", filetypes=[("pdf files", "*.pdf")])

    def _merge_pdfs(self):
        pdf_writer = PdfFileWriter()
        for file_path in self.file_paths:
            pdf = PdfFileReader(file_path)
            for page in range(pdf.getNumPages()):
                pdf_writer.addPage(pdf.getPage(page))

        with open("outFile.pdf", 'wb') as output:
            pdf_writer.write(output)

    def complete_merge_tasks(self):
        """completes merge pdf related tasks """
        self._merge_pdfs()  # need to validate input here
        self._display_info_texts()

    def _display_info_texts(self):
        self.info_text.grid(row=6, column=3)
        self.info_text.configure(
            text="Task Complete!", foreground="green")

    def display_UI(self):
        self.select_btn.grid(row=0, column=0)
        self.merge_btn.grid(row=5, column=0)

    def _get_file_paths(self):
        """gets file path of pdf for splitting"""
        self.select_pdfs()
        self.file_path_label.configure(
            text=f'{len(self.file_paths)} Files')
        self.file_path_label.grid(row=0, column=1)
