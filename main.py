from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

# user entered values
amount = float(input("Hey user, enter the bill amount: "))
period = input("Hey user, enter the period: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house?, "))

name2 = input("What is your name? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house?, "))

bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(bill, flatmate1))
print("Total paid is: ", flatmate1.pays(bill, flatmate2) + flatmate2.pays(bill, flatmate1))

pdf_report = PdfReport(f"{bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill)

fileshare = FileSharer(pdf_report.filename)
print(fileshare.share())