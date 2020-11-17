from PDFWorker import PDFWorker
from UI import UI


class PDFModipy:
    """Overall class to manage UI and behavior"""

    def __init__(self):
        self.UI = UI()
        self.pdf_worker = PDFWorker()
        self.main_loop = self.UI.root.mainloop

    def display_UI(self):
        """Displays the UI"""
        self.UI.select_btn.grid(row=1, column=0)

        self.UI.start_page_label.grid(row=2)
        self.UI.start_page.grid(row=2, column=1)
        self.UI.end_page_label.grid(row=3)
        self.UI.end_page.grid(row=3, column=1)
        self.UI.split_btn.grid(row=4, column=0)

        # if(len(self.pdf_worker.file_path) > 0):
        #     print("firing")
        #     self.UI.file_path_label.configure(text=self.pdf_worker.file_path)
        #     self.UI.file_path_label.grid(row=0)

    def attach_logic(self):
        """attaches commands to buttons on UI"""
        self.UI.select_btn.configure(
            command=self._show_file_path)
        self.UI.split_btn.configure(
            command=lambda: self.pdf_worker.split_pdf(3, 6))

    def _show_file_path(self):
        self.pdf_worker.select_pdf()
        self.UI.file_path_label.configure(
            text=self.pdf_worker.file_path)
        self.UI.file_path_label.grid(row=0)

    def run_program(self):
        """runs the main program"""
        self.display_UI()
        self.attach_logic()
        self.main_loop()


if __name__ == "__main__":
    pdf_modipy = PDFModipy()
    pdf_modipy.run_program()
