hrs = input("Enter Hours:")
h = float(hrs)
rate = 10.50
overtime = 10.50 * 1.5
if h <= 40 :
    pay = h * rate
elif h > 40 :
    pay = (40 * rate) + ((h - 40) * overtime)
print(pay)