import socket

target_host = "google.com"  # replace with the hostname or IP address of the target computer
target_port = 80  # replace with the port number of the service you want to connect to

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the target host
client.connect((target_host, target_port))

# Send a message to the target host
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive and print the response
response = client.recv(4096)
print(response)
