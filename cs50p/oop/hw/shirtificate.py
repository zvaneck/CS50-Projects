from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.image("shirtificate.png", 10, 70, 190)
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0, 30, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.set_font("helvetica", "B", 20)
        self._pdf.cell(0, 200, f"{name} took CS50", align="C")

    def save(self, name):
        self._pdf.output("shirtificate.pdf")

name = input("Name: ")
shirtificate = PDF(name)
shirtificate.save("shirtificate.pdf")