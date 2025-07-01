counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
    # use 'get' to provide a default value of 0 when the key is not in the dictionary.
print(counts)
# Output: {'csev': 2, 'cwen': 2, 'zqian': 1}. It also looks like a constant. 