from PyPDF2 import PdfFileReader, PdfFileWriter


class PDfWorker:
    def __init__(self, file_path):
        self.file_path = file_path

    def split_pdf(self, start_page, end_page):
        pdf = PdfFileReader(self.file_path)
        pdf_writer = PdfFileWriter()
        for page in range(start_page-1, end_page):
            pdf_writer.addPage(pdf.getPage(page))

        with open("outFile.pdf", 'wb') as output:
            pdf_writer.write(output)

    def merge_pdf():
        print("merge")

    def encrypt_pdf():
        print("encrypt")
