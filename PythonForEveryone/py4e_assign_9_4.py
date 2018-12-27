#Import Files
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#Declaration of Variables
countfrom = dict()
mostemail = None
mostcount = None

#Line counter
for line in handle:
    line = line.split()
    #Gaurdian break
    if len(line) < 1 or line[0] != 'From': continue
    email = line[1]
    countfrom[email] = countfrom.get(email,0) + 1

#Find the most received emails
for k,v in countfrom.items():
    if mostemail is None or mostcount < v:
        mostemail = k
        mostcount = v

print(mostemail,mostcount)

