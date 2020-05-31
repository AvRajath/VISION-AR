import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.43.113', 9050))
sock.listen(1)  # allow only 1 connection
connection, client_address = sock.accept()
try:
  # Receive the data
  while True:
    data = connection.recv(128)   # the buffer in this example is 128 bytes
    if data:
    	print(data)
    	
    #connection.sendall(data)
    else:
      continue

finally:
  # Clean up the connection
  connection.close()