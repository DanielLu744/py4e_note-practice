import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Inputs
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) 

# Loop through the required number of times
for i in range(count):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all anchor tags
    tags = soup('a')

    # Move to the link at the given position (1-based, so subtract 1)
    url = tags[position - 1].get('href', None)

# Final retrieval
print("Retrieving:", url)
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Extract and print the last name from the final URL
import re
name = re.findall(r'known_by_(.+)\.html', url)
# print(name)
print("The answer to the assignment is:", name[0])

# link: http://py4e-data.dr-chuck.net/known_by_Cadan.html 