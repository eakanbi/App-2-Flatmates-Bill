from fpdf import FPDF

class Bill:

    """
    Object that contains data about a bill, such as total amount 
    and period of the bill.
    """

    def __init__(self, amount, period): 
        self.amount = amount
        self.period = period


class Flatemate:
    """
    Create a flatemate person who lives in the flate and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatemate2):
        weight = self.days_in_house/(self.days_in_house + flatemate2.days_in_house)
        to_pay =  bill.amount * weight
        return to_pay


    
class PDFReport:
    """
    Creates a PDF file that cotains data about the flatemates such as the name, amount due
    and the period of time
    """

    def __init__(self, filename) -> None:
        self.filename = filename

    def generate(self, flatmate1, flatmate2 , bill):

        flatmate1_pay =  str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1),2))
       
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Insert Title
        pdf.set_font(family="Times", size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        #Insert Period label and value
        pdf.cell(w=100, h=40, txt="Period", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)
        
        #Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=1, ln=1)
        
        #Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=1, ln=1)

        pdf.output(self.filename)


the_bill = Bill(120, "April 2021")
john = Flatemate("John", 20)
marry = Flatemate("Mary", 25)
print(f"John pays ${john.pays(the_bill, flatemate2=marry)}")
print(f"Mary pays ${marry.pays(the_bill, flatemate2=john)}")

pdf_report = PDFReport("Report1.pdf")
pdf_report.generate(john, marry, the_bill)
