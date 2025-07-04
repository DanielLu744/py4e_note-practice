import re

# Ask user for file name
filename = input("Enter file: ")

try:
    handle = open(filename)
except:
    print(f"File cannot be opened: {filename}")
    quit()

# List to store all extracted numbers
numbers = []

# Loop through each line and search for matches
for line in handle:
    line = line.strip()
    match = re.findall(r'^New Revision: (\d+)', line)
    if match:
        numbers.append(int(match[0]))

# Calculate average
if numbers:
    average = sum(numbers) / len(numbers)
    print(int(average))  # Truncate to integer
else:
    print("No matching lines found.")
