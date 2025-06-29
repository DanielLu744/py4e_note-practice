fname = input("Enter file name: ").strip()
fh = open(fname)
lst = []

for line in fh:
    words = line.split()  # split the line into a list of words
    for word in words:
        if word not in lst:
            lst.append(word) # avoid duplicates, add new words 

lst.sort()  # sort the list alphabetically
print(lst)