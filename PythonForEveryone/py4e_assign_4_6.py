def computepay(hours,rate) :
    if hours <= 40 :
        return hours * rate
    elif hours > 40 :
        return (40 * rate) + ((hours - 40) * (rate * 1.5))

rawhrs = input("Enter Hours: ")
rawrate = input("Enter Rate: ")
hrs = float(rawhrs)
rate = float(rawrate)

print(computepay(hrs,rate))