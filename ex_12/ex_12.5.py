import socket

try:
    url = input('Enter URL: ').strip()
    if not url.startswith('http://'):
        raise ValueError('URL must start with http://')

    # Extract host and path
    parts = url.split('/')
    host = parts[2]
    path = '/' + '/'.join(parts[3:])

    # Create socket and connect
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    # Send GET request
    cmd = f'GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n'.encode()
    mysock.send(cmd)

    # Receive response
    received = b''
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        received += data

    mysock.close()

    # Find end of headers (\r\n\r\n marks the blank line)
    decoded = received.decode()
    split_pos = decoded.find('\r\n\r\n')
    
    if split_pos != -1:
        body = decoded[split_pos + 4:]  # skip past \r\n\r\n
        print(body)
    else:
        print("No headers found, or malformed response.")

except Exception as e:
    print('Error:', e)
    