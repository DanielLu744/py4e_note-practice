import re

# Step 1: Open the file (replace with the correct filename if needed)
filename = "regex-sum.txt"
handle = open(filename)

# Step 2: Read the file and find all numbers
numbers = []
for line in handle:
    found = re.findall(r'[0-9]+', line)
    numbers.extend(found)

# Step 3: Convert strings to integers and sum them
int_numbers = [int(num) for num in numbers]
total = sum(int_numbers)

print("Sum: ", total)
