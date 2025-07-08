import urllib.request
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors (if needed)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    url = input('Enter URL: ').strip()
    html = urllib.request.urlopen(url, context=ctx).read()

    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all paragraph tags
    tags = soup('p')
    print('Paragraph count:', len(tags))

except Exception as e:
    print('Error:', e)