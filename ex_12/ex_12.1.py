import socket

try:
    url = input('Enter URL: ').strip()
    if not url.startswith('http://'):
        raise ValueError('URL must start with http://')

    # Split the URL into parts
    parts = url.split('/')
    host = parts[2]  # e.g. data.pr4e.org
    path = '/' + '/'.join(parts[3:])  # e.g. /romeo.txt

    # Create socket and connect to the host
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    # Form HTTP GET request
    cmd = f'GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n'.encode()
    mysock.send(cmd)

    # Receive and display the response
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

    mysock.close()

except Exception as e:
    print('Error:', e)