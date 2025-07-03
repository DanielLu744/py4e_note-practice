name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line = line.strip()  

    if line.startswith('From '):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1   
        # print(counts) --- (key, value)

lst = list()
for email, count in counts.items():
    tup = (count, email)  # new tuple
    lst.append(tup)  # appending the tuple to the list
    # print(lst)

lst = sorted(lst, reverse=True)  # sort in descending order
# print(lst)

top_count, top_email = lst[0]
print(top_email, top_count)
