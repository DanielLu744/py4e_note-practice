name = 'mbox-short.txt'

# Open the file
handle = open(name)

# mpety dictionary
counts = dict()

# Access the file
for line in handle:
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        # print(words)
        if len(words) >= 3: 
            day = words[2]
            counts[day] = counts.get(day, 0) + 1

print(counts)
