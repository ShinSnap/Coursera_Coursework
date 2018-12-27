name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counter = dict()

for line in handle:
    line = line.split()
    if len(line) < 1 or line[0] != 'From': continue
    time = line[5].split(':')
    hour = time[0]
    counter[hour] = counter.get(hour,0) + 1

for k,v in sorted(counter.items()):
    print(k,v)