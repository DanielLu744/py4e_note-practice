# the top 10 most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
# above, counts in the histogram

# does everything for the sorting part
print(sorted([(v,k) for k,v in counts.items()])) 