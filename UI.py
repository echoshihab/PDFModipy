from tkinter import *


class UI:
    """A class to set up UI"""

    def __init__(self):
        self.root = Tk()
        self.root.title = ("PDFModipy")
        self.root.geometry = ("1024X800")
        self.select_btn = Button(self.root, text="Select File")
        self.start_page = Entry(self.root, width=10)
        self.end_page = Entry(self.root, width=10)
        self.split_btn = Button(self.root, text="Split",
                                )
        self.merge_btn = Button(self.root, text="Merge")
        self.encrypt_btn = Button(self.root, text="Encrypt")


# command=lambda: PDfWorker(path).split_pdf(3, 6)
