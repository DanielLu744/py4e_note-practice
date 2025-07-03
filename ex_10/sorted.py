d = {'a':10, 'c':22, 'b':1}
d.items() # get a list of tuples from the dictionary
# dict_items([('a', 10), ('c', 22), ('b', 1)])

s = sorted(d.items()) # sort the tuples
print(s)
# [('a', 10), ('b', 1), ('c', 22)]

for k, v in sorted(d.items()): # sorted by key
    print(k, v)