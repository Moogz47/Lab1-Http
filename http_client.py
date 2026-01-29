"""
Student Name: Julila Mpesha
Student ID: (N01751205)
CPAN-226 Lab 1
"""

from socket import *

server_name = 'gaia.cs.umass.edu'
server_port = 80

# 1. Create a TCP socket (IPv4)
# Hint: Use AF_INET for IPv4 and SOCK_STREAM for TCP
client_socket = socket(AF_INET, SOCK_STREAM)

# 2) Connect to the server
client_socket.connect((server_name, server_port))

# 3. Prepare the HTTP request
# Critical: HTTP requires carriage return & new line (\r\n) at the end of headers
# The double \r\n\r\n indicates the end of the header section.
request = (
    "GET /kurose_ross/interactive/index.php HTTP/1.1\r\n"
    "Host: gaia.cs.umass.edu\r\n"
    "Connection: close\r\n"
    "\r\n"
)

# 4) Send the request
client_socket.sendall(request.encode())

# 5) Receive the response
response_chunks = []
while True:
    data = client_socket.recv(4096)
    if not data:
        break
    response_chunks.append(data)

# 6) Decode and print the result
full_response = b"".join(response_chunks).decode(errors="replace")
print(full_response)

# 7) Close the connection
client_socket.close()