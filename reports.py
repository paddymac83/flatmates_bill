import webbrowser
import os
from fpdf import FPDF
from filestack import Client


class PdfReport:
    """
    Object contains info in report on names, amount paid, and month
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        pdf = FPDF(orientation='P',
                   unit='pt',
                   format='A4')

        pdf.add_page()

        # add image for report
        pdf.image("files/house.png", w=30, h=30)

        # add some text
        pdf.set_font(family='Times', size=24, style='B')

        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C',
                 ln=1)

        pdf.set_font('Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font('Times', size=12)
        flatmate1_pays = str(round(flatmate1.pays(bill, flatmate2), 2))
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pays, border=0, ln=1)

        flatmate2_pays = str(round(flatmate2.pays(bill, flatmate1), 2))
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pays, border=0, ln=1)

        # open in web browser
        os.chdir("files")

        pdf.output(self.filename)
        webbrowser.open(self.filename)

class FileSharer():

    def __init__(self, file_path, api_key = 'AM6VC2tlMQ8G9cYDgOrX4z'):
        self.api_key = api_key
        self.file_path = file_path

    def share(self):
        client = Client(self.api_key)

        new_filelink = client.upload(filepath = self.file_path)

        return new_filelink.url
        