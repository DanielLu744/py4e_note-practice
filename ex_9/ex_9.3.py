name = input('Enter the file: ')
if len(name) < 1: 
    name = 'mbox-short.txt'

handle = open(name)

counts = dict()

for line in handle:
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        # print(words)
        email = words[1]
        # print(email)
        counts[email] = counts.get(email, 0) + 1

print(counts) 
