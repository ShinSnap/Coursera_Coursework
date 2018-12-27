text = "X-DSPAM-Confidence:    0.8475"
numpos = text.find("0")
number = float(text[numpos:])
print(number)