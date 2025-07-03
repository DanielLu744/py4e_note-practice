import string

# Step 1: Get file name and open it
fname = input("Enter file name: ")
fhand = open(fname)

# Step 2: Create a dictionary to hold letter counts
counts = dict()

# Step 3: Process each line
for line in fhand:
    line = line.lower()  # convert to lowercase
    for char in line:
        if char in string.ascii_lowercase:  # only count a-z
            counts[char] = counts.get(char, 0) + 1

# Step 4: Create a list of (count, letter) tuples and sort descending
letter_list = []
for letter, count in counts.items():
    letter_list.append((count, letter))

letter_list.sort(reverse=True)  # sort by count descending

# Step 5: Print results
for count, letter in letter_list:
    print(letter, count)
