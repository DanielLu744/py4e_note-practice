# Ask for filename; use default if input is empty
filename = input("Enter a file name: ")
if len(filename) < 1:
    filename = "mbox-short.txt"

# Open the file
handle = open(filename)

# Create an empty dictionary to store domain counts
domain_counts = dict()

# Loop through each line in the file
for line in handle:
    line = line.strip()

    # Only look at lines that start with "From "
    if line.startswith("From "):
        words = line.split()
        email = words[1]         # Get the full email address
        domain = email.split('@')[1]  # Get the part after the '@'
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

# Print the dictionary of domain counts
print(domain_counts)
