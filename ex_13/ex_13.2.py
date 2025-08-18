import urllib.request
import json 

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2223506.json'

print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

info = json.loads(data)
print('User count', len(info))

# Extract the list of comments
comments = info["comments"]
# print(comments)

# Loop through and add up the counts
total = 0
for item in comments:
    total += item["count"]

print('Count:', len(comments))
print('Sum:', total)