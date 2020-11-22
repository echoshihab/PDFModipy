from tkinter import *
from tkinter import ttk


class UI:
    """A class to set up UI"""

    def __init__(self):
        self.root = Tk()
        self.root.title("PDFModipy")
        self.root.geometry("300x180")

        self.tab_parent = ttk.Notebook(self.root)
        self.split_tab = ttk.Frame(self.tab_parent)
        self.merge_tab = ttk.Frame(self.tab_parent)
        self.encrypt_tab = ttk.Frame(self.tab_parent)
        self._add_tabs()

    def _add_tabs(self):
        self.tab_parent.add(self.split_tab, text="Split PDF")
        self.tab_parent.add(self.merge_tab, text="Merge PDF")
        self.tab_parent.add(self.encrypt_tab, text="Encrypt PDF")
