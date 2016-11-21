import socket
import sys
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
port = int(os.environ.get('PORT', 8000))
server_address = ('0.0.0.0', port)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
packet_size = 65000

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(packet_size)
            data = data.strip('\r\n');
            if data:
                print >>sys.stderr, 'received "%s"' % data
                if 'PACKET_SIZE:' in data:
                    packet_size = int(data.split(':')[1])
                    print >>sys.stderr, 'packet size set to %s' % packet_size
                elif 'CLOSE_SOCKET' in data:
                    break
                else:
                    print >>sys.stderr, 'sending data back to the client'
                    connection.send(data)
            #else:
            #    print >>sys.stderr, 'no more data from', client_address
            #    break

    finally:
        # Clean up the connection
        print >>sys.stderr, 'closing the connection'
        connection.close()

