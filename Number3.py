name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

count = dict()
lst = []

for line in handle:
    words = line.split()
    if not line.startswith('From '): continue
    words = line.split()
    hour = words[5].split(':')
    count[hour[0]] = count.get(hour[0], 0) + 1

for k, v in count.items():
    lst.append((k, v))
lst.sort()
for k, v in lst:
    print(k, v)
