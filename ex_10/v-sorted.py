# sorted by value(numbers) instead of key(words/str)
d = {'a':10, 'c':22, 'b':1}
tmp = list()
for k, v in d.items():
    tmp.append((v, k))
print(tmp)
# [(10, 'a'), (22, 'c'), (1, 'b')]

tmp = sorted(tmp, reverse=True) # sorted in descending order
print(tmp)
# [(22, 'c'), (10, 'a'), (1, 'b')]