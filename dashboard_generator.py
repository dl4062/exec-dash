# dashboard_generator.py
import os
import csv
import datetime
import itertools
from operator import itemgetter
import operator
import matplotlib.pyplot as plt

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71






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

sales_prices = [float(row["sales price"]) for row in rows]
total_sales = sum(sales_prices)

print("-----------------------")
print("TOTAL MONTHLY SALES: ", to_usd(total_sales))

sold_products = []

for product in rows:
    sold_products.append(product["product"])

sold_products = set(sold_products)

combined_list = []

sorted_products = sorted(rows, key=itemgetter("product"))

product_groups = itertools.groupby(sorted_products, key=itemgetter("product"))

for product, product_rows in product_groups:
    month_sales = sum([float(row["sales price"]) for row in product_rows])
    combined_list.append({"name": product, "monthly sales": month_sales})

sorted_list = sorted(combined_list, key=itemgetter("monthly sales"), reverse=True)

print("-----------------------")
print("TOP SELLING PRODUCTS:")

rank = 0
for top_selling in sorted_list:
    rank = rank + 1
    print(str(rank) + ".", top_selling["name"] + ":", to_usd(top_selling["monthly sales"]))
    

labels = []
sizes = []

for name in sorted_list:
    labels.append(name["name"])
 
for price in sorted_list:
    sizes.append(price["monthly sales"]) #removed str()


# https://stackoverflow.com/questions/6170246/how-do-i-use-matplotlib-autopct#:~:text=autopct%20enables%20you%20to%20display,set%20to%20the%20string%20'%25.
def make_autopct(sizes):
    def my_autopct(pct):
        total = sum(sizes)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  (${v:d})'.format(p=pct,v=val)
    return my_autopct

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct = make_autopct(sizes))
ax1.axis('equal')
plt.show()

