import urllib.request
import json

# Prompt for URL (default to sample if blank)
url = input('Enter location: ').strip()
if not url:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)
data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')

# Parse JSON
js = json.loads(data)

# js['comments'] is a list of dicts like {'name': 'Matthias', 'count': 97}
counts = []  # Step 4: Create an empty list to store all the counts

# Step 5: Get the list of all comments from the JSON
comment_list = js.get('comments', [])

# Step 6: Loop through each comment in the list
for item in comment_list:
    # Step 6a: Get the 'count' number from this comment
    number = item['count']
    # print(number)

    # Step 6b: Put the number into the counts list
    counts.append(number)

print('Count:', len(counts))
print('Sum:', sum(counts))
