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
        self.UI.select_btn.pack()
        self.UI.split_btn.pack()

    def attach_logic(self):
        """attaches commands to buttons on UI"""
        self.UI.select_btn.configure(command=self.pdf_worker.select_pdf)
        self.UI.split_btn.configure(
            command=lambda: self.pdf_worker.split_pdf(3, 6))

    def run_program(self):
        """runs the main program"""
        self.display_UI()
        self.attach_logic()
        self.main_loop()


if __name__ == "__main__":
    pdf_modipy = PDFModipy()
    pdf_modipy.run_program()
