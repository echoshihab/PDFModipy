from PDFWorker import PDFWorker
from UI import UI
import webbrowser
import os


class PDFModipy:
    """Overall class to manage UI and behavior"""

    def __init__(self):
        self.UI = UI()
        self.pdf_worker = PDFWorker()
        self.main_loop = self.UI.root.mainloop

    def display_UI(self):
        """Displays the UI"""
        self.UI.select_btn.grid(row=0, column=0)
        self.UI.start_page_label.grid(row=3, sticky='W')
        self.UI.start_page.grid(row=3, column=1, sticky='W')
        self.UI.end_page_label.grid(row=4, sticky='W')
        self.UI.end_page.grid(row=4, column=1, sticky='W')
        self.UI.split_btn.grid(row=5, column=0)
        self.UI.tab_parent.pack(fill='both', expand=1)

    def attach_logic(self):
        """attaches commands to buttons on UI"""
        self.UI.select_btn.configure(
            command=self._get_file_path)
        self.UI.split_btn.configure(command=self._split_pdf)

    def _split_pdf(self):
        """splits pdf"""
        self.UI.info_text.grid(row=6, column=3)
        self.pdf_worker.split_pdf(
            int(self.UI.start_page.get()), int(self.UI.end_page.get()))
        self._clean_up_page_entry()
        self.UI.info_text.configure(text="Task Complete!", foreground="green")
        self._open_file_directory()

    def _clean_up_page_entry(self):
        """blanks out start and end page text boxes"""
        self.UI.start_page.delete(0, "end")
        self.UI.end_page.delete(0, "end")

    def _get_file_path(self):
        """gets file path of pdf"""
        self.pdf_worker.select_pdf()
        self.UI.file_path_label.configure(
            text=self._shorten_file_name())
        self.UI.file_path_label.grid(row=0, column=1)

    def _shorten_file_name(self):
        file_name = self.pdf_worker.file_path.split('/')[-1]
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
