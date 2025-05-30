fname = input("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
total = 0.0

for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        colon_pos = line.find(":")
        number_str = line[colon_pos + 1:].strip()
        try:
            number = float(number_str)
        except:
            continue
        total = total + number 
        count = count + 1 

if count > 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No matching lines found.")