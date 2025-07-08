import socket      # Import the socket library to use network features

# Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the web server at data.pr4e.org, using port 80 (HTTP)
mysock.connect(('data.pr4e.org', 80))

# Prepare an HTTP GET request to ask for /romeo.txt using HTTP 1.0
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

# Send the HTTP request to the server
mysock.send(cmd)

# Loop to receive data in 512-byte chunks
while True:
    data = mysock.recv(512)  # Read up to 512 bytes of response from server
    if (len(data) < 1):      # If no more data is received, break the loop
        break
    print(data.decode())     # Decode bytes into string and print it

# Close the socket connection
mysock.close()