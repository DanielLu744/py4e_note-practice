import re

# Ask the user for a regular expression
regex = input("Enter a regular expression: ")

# Open the file
filename = "mbox.txt"
try:
    file = open(filename)
except:
    print(f"Cannot open file: {filename}")
    quit()

# Count matching lines
count = 0
for line in file:
    line = line.rstrip()
    if re.search(regex, line):
        count += 1

print(f"{filename} had {count} lines that matched {regex}")
