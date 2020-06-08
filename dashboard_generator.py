# dashboard_generator.py
import os

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

## prints data in a readable list - https://realpython.com/working-with-files-in-python/#directory-listing-in-modern-python-versions

data = os.path.join(os.path.dirname(__file__), "data", "monthly-sales")

print("Please select a monthly data package from the list below:")

monthly_data = (os.listdir(data))
for single_month in monthly_data:
    print(single_month)

