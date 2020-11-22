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
        self.pdf_splitter.display_ui()
        self._display_encrypt_UI()
        self.UI.tab_parent.pack(fill='both', expand=1)

    def _display_encrypt_UI(self):
        self.pdf_encrypt.select_btn.grid(row=0, column=0)
        self.pdf_encrypt.encrypt_password_label.grid(
            row=2, column=0, sticky='W')
        self.pdf_encrypt.encrypt_password.grid(row=2, column=1, sticky='W')
        self.pdf_encrypt.confirm_password_label.grid(
            row=3, column=0, sticky='W')
        self.pdf_encrypt.confirm_password.grid(row=3, column=1, sticky='W')
        self.pdf_encrypt.encrypt_btn.grid(row=4, column=0)

    def attach_logic(self):
        """attaches commands to buttons on UI"""
        self.pdf_splitter.split_btn.configure(
            command=self._split)
        self.pdf_encrypt.encrypt_btn.configure(
            command=self._complete_encrypt_tasks)

    def _split(self):
        self.pdf_splitter.complete_split_tasks()
        self._open_file_directory()

    def _complete_encrypt_tasks(self):
        self.UI.info_text_encrypt.grid(row=6, column=3)
        self.pdf_encrypt.encrypt_pdf("password")
        self.UI.info_text_encrypt.configure(
            text="Task Complete!", foreground="green")
        self._open_file_directory()

    def _get_file_path_encrypt(self):
        self.pdf_encrypt.select_pdf()
        self.UI.file_path_label_encrypt.configure(
            text=self._shorten_file_name())
        self.UI.file_path_label_encrypt.grid(row=0, column=1)

    def _shorten_file_name(self):
        file_name = self.pdf_splitter.file_path.split('/')[-1]
        return file_name if len(file_name) < 36 else file_name[:36] + "..."

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
