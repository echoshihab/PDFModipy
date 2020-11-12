
from tkinter import *
from pdfModipy import *
from PDFWorker import *
from tkinter import filedialog


root = Tk()
root.title = ("PDFModipy")
root.geometry = ("600x400")


def select_file():
    global path
    path = filedialog.askopenfilename(
        initialdir="/", title="Select a file", filetypes=(("pdf files", "*.pdf"), ("all files", "*.*")))
    label = Label(root, text=path).pack()


# UI
select_btn = Button(root, text="Select File", command=select_file).pack()
start_page = Entry(root, width=10)
end_page = Entry(root, width=10)
split_btn = Button(root, text="Split",
                   command=lambda: PDfWorker(path).split_pdf(3, 6)).pack()
merge_btn = Button(root, text="Merge", command=PDfWorker.merge_pdf).pack()
encrypt_btn = Button(root, text="Encrypt", command=PDfWorker.encrypt_pdf).pack

root.mainloop()
