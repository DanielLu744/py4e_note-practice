name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

handle = open(name)

counts = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        # print(words)
        time = words[5]
        hour = time.split(':')[0]
        counts[hour] = counts.get(hour, 0) + 1
        # print(counts)

# create a list of tuples from the dictionary and sort it
sorted_counts = sorted(counts.items())  # creates and sorts list of tuples
# print(sorted_counts)

# print the result
for hour, count in sorted_counts:
    print(hour, count)
