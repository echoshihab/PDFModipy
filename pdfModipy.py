from pdfSplitter import PDFSplitter
from pdfEncrypt import PDFEncrypt
from UI import UI
import webbrowser
import os


class PDFModipy:
    """Overall class to manage UI and behavior"""

    def __init__(self):
        self.UI = UI()
        self.pdf_splitter = PDFSplitter(self.UI)
        self.pdf_encrypt = PDFEncrypt(self.UI)
        self.main_loop = self.UI.root.mainloop

    def display_UI(self):
        """Displays the UI"""
        self.pdf_splitter.display_UI()
        self.pdf_encrypt.display_UI()
        self.UI.tab_parent.pack(fill='both', expand=1)

    def attach_logic(self):
        """attaches commands to buttons on UI"""
        self.pdf_splitter.split_btn.configure(
            command=self._split)
        self.pdf_encrypt.encrypt_btn.configure(
            command=self._encrypt)

    def _split(self):
        self.pdf_splitter.complete_split_tasks()
        self._open_file_directory()  # have to prevent open file directory on errors

    def _encrypt(self):
        success = self.pdf_encrypt.complete_encrypt_tasks()
        if(success):
            self._open_file_directory()

    def _open_file_directory(self):
        location = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        os.system(f'start {os.path.realpath(location)}')

    def run_program(self):
        """runs the main program"""
        self.display_UI()
        self.attach_logic()
        self.main_loop()


if __name__ == "__main__":
    pdf_modipy = PDFModipy()
    pdf_modipy.run_program()
