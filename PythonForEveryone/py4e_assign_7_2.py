# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

total = 0
linecount = 0

for line in fh:
    if not line.startswith('X-DSPAM-Confidence:') : continue
    linepos = line.find(':')
    line = line[linepos+1:]
    total = float(line) + total
    linecount = linecount + 1

average = total / linecount
print('Average spam confidence:',average)

x = range(5)
print(x)