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

    def generate(self, flatemate1, flatmate2 , bill):
        pass


the_bill = Bill(120, "March 2021")
john = Flatemate("John", 20)
marry = Flatemate("Mary", 25)
print(john.pays(the_bill, flatemate2=marry))