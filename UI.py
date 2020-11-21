from tkinter import *
from tkinter import ttk, IntVar


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

        # Split Tab items
        self.select_btn_split = Button(self.split_tab, text="Select File")
        self.file_path_label_split = Label(self.split_tab)

        self.start_page = Entry(self.split_tab, width=10)
        self.start_page_label = Label(self.split_tab, text="Start Page")

        self.end_page_label = Label(self.split_tab, text="End Page")
        self.end_page = Entry(self.split_tab, width=10)

        self.split_btn = Button(self.split_tab, text="Split")

        self.info_text_split = Label(self.split_tab, text="working...")

        # Merge Tab Items
        self.merge_btn = Button(self.merge_tab, text="Merge")

        # Encrypt Tab Items
        self.select_btn_encrypt = Button(self.encrypt_tab, text="Select File")
        self.file_path_label_encrypt = Label(self.split_tab)

        self.encrypt_password = Entry(self.encrypt_tab, show="*", width=10)
        self.encrypt_password_label = Label(self.encrypt_tab,  text="Password")
        self.confirm_password_label = Label(
            self.encrypt_tab, text="Confirm Password")
        self.confirm_password = Entry(self.encrypt_tab, show="*", width=10)
        self.info_text_encrypt = Label(self.split_tab, text="working...")
        self.encrypt_btn = Button(self.encrypt_tab, text="Encrypt")

    def _add_tabs(self):
        self.tab_parent.add(self.split_tab, text="Split PDF")
        self.tab_parent.add(self.merge_tab, text="Merge PDF")
        self.tab_parent.add(self.encrypt_tab, text="Encrypt PDF")
