# dashboard_generator.py
import os
import csv
import datetime




print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

data = os.path.join(os.path.dirname(__file__), "data", "monthly-sales")


monthly_data = (os.listdir(data))
for single_month in monthly_data:
    print(single_month)

choice = input("Please select a monthly data package from the list above: ")

## data validation part

while os.path.isfile(os.path.join(data, choice)) == False:
    if os.path.isfile(os.path.join(data, choice)) == False:
        choice = input("This file does not exist in this folder - Please select a monthly data package from the specified list: ")
    else:
        break
        
# making the csv file readable

csv_filepath = os.path.join("data", "monthly-sales", choice)

rows = []

with open(csv_filepath, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        rows.append(dict(row))

# printing the correct month

month = int((choice[10:12]))
year = int((choice[6:10]))

month_year = datetime.date(year,month,1)

print("-----------------------")
print(month_year.strftime("%B, %Y"))

print("-----------------------")
print("CRUNCHING THE DATA...")

