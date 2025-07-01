# Ask the user for a filename; use "mbox-short.txt" as default if input is empty
name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

# Open the file for reading
handle = open(name)

# Create an empty dictionary to count email occurrences
counts = dict()

# Loop through each line in the file
for line in handle:
    line = line.strip()   # Remove leading/trailing whitespace

    # Only process lines that start with "From " (note the space)
    # These are the lines that contain email senders (e.g., "From stephen.marquard@uct.ac.za ...")
    if line.startswith('From '):   # Note: space after 'From'
        words = line.split()   # Split the line into words
        email = words[1]       # The second word is the email address/the sender
        counts[email] = counts.get(email, 0) + 1   # Increment count for this email address

# Initialize variables to track the most frequent email and count
bigemail = None
bigcount = None

# Loop through the dictionary to find the email with the highest count
for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigemail = email   # Update most frequent email
        bigcount = count   # Update highest count

# Print the result: the most prolific sender and how many messages they sent
print(bigemail, bigcount) 
