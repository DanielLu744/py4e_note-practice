import urllib.request

try:
    url = input('Enter URL: ').strip()

    # Open and read the URL
    response = urllib.request.urlopen(url)
    data = response.read()

    # Decode the bytes to a string
    text = data.decode()

    # Display up to 3000 characters
    print(text[:3000])

    # Display total character count
    print(f"\nTotal characters received: {len(text)}")

except Exception as e:
    print('Error:', e)