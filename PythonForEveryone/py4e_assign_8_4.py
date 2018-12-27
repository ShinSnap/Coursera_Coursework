fname = input("Enter file name: ")
fh = open(fname)
words = list()
for line in fh:
    sline = line.split()
    for word in sline:
        if word in words: continue
        words.append(word)

words.sort()
print(words)