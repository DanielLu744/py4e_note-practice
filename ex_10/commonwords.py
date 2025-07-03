# the top 10 most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
# above, counts in the histogram

# starts sorting
lst = list()
for key, val in counts.items():
    newtup = (val, key) # making a tuple
    lst.append(newtup)  # appending the tuple to the list

lst = sorted(lst, reverse=True)
# print(lst)

for val, key in lst[:10]: 
    print(key, val)