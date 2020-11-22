from tkinter import *


class PDFMerger:
    def __init__(self, UI):
        self.file_paths = []
        self.merge_btn = Button(UI.merge_tab, text="Merge")
