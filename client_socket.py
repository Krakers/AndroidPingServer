import socket
import sys


def send_data(message, packet_size):

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect the socket to the port where the server is listening
	server_address = ('localhost', 1337)
	print >>sys.stderr, 'connecting to %s port %s' % server_address
	sock.connect(server_address)

	try:

	    # Send data
	    print >>sys.stderr, 'sending "%s"' % message
	    sock.sendall(message)

	    # Look for the response
	    amount_received = 0
	    amount_expected = len(message)

	    while amount_received < amount_expected:
	        data = sock.recv(packet_size)
	        amount_received += len(data)
	        print >>sys.stderr, 'received "%s"' % data

	finally:
	    print >>sys.stderr, 'closing socket'
	    sock.close()


packet_size = 4096
set_size = 'PACKET_SIZE:4096'
send_data(set_size, packet_size)

message = 'This is the message.  It will be repeated.'
send_data(message, packet_size)