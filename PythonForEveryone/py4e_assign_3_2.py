score = input("Enter Score: ")

try :
    score = float(score)
except :
    print("Error: Input a numerical value between 0 and 1.0")
    quit(1)

if score > 1.0 :
    print("Score is greater that allow scoring range (0 to 1.0)")
    quit(1)
elif score < 0 :
    print("Score is greater that allow scoring range (0 to 1.0)")
    quit(1)
else :
    if score >= 0.9 :
        print("A")
    elif score >= 0.8 :
        print("B")
    elif score >= 0.7 :
        print("C")
    elif score >= 0.6 :
        print("D")
    elif score < 0.6 :
        print("F")