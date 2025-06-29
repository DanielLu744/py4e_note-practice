fname = input("Enter file name: ").strip()
fh = open(fname)
# fle = fh.read()
# print(fle)

count = 0
for line in fh : 
    line = line.strip()
    if line.startswith('From '):  # Only lines starting with 'From '
        words = line.split() 
        if len(line) >=2 :   # Safe check
            print(words [1]) # Print the second word (email)
            count += 1

print("There were", count, "lines in the file with From as the first word")