import sys

name = sys.argv[1]
phone = sys.argv[2]
bill = sys.argv[3]
date = sys.argv[4]

p1 = sys.argv[5]
q1 = int(sys.argv[6])
price1 = float(sys.argv[7])

p2 = sys.argv[8]
q2 = int(sys.argv[9])
price2 = float(sys.argv[10])

total1 = q1 * price1
total2 = q2 * price2

total = total1 + total2

print("\n--------- GROCERY BILL ---------")
print("Customer Name:", name)
print("Phone Number:", phone)
print("Bill Number:", bill)
print("Bill Date:", date)

print("\nProduct 1:", p1)
print("Quantity:", q1)
print("Price:", price1)
print("Subtotal:", total1)

print("\nProduct 2:", p2)
print("Quantity:", q2)
print("Price:", price2)
print("Subtotal:", total2)

print("\nTotal Amount:", total)
print("--------------------------------")