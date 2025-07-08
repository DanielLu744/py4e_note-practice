import socket

try:
    url = input('Enter URL: ').strip()
    if not url.startswith('http://'):
        raise ValueError('URL must start with http://')

    # Split URL
    parts = url.split('/')
    host = parts[2]
    path = '/' + '/'.join(parts[3:])

    # Create and connect socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = f'GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n'.encode()
    mysock.send(cmd)

    total_data = b''
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        total_data += data

    mysock.close()

    decoded_data = total_data.decode()
    # Show only first 3000 characters
    print(decoded_data[:3000])
    # Print total character count
    print(f"\nTotal characters received: {len(decoded_data)}")

except Exception as e:
    print('Error:', e)