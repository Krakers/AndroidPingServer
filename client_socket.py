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

message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus hendrerit odio ultrices tempus auctor. Cras eu quam nec massa tempus dictum. Nam vel semper tortor, at fringilla sem. Fusce ac molestie tellus. Morbi sed dapibus lectus. Suspendisse convallis, purus eget feugiat ultrices, erat erat tincidunt tortor, vitae lacinia justo sem vel eros. Duis nec neque sagittis, ultrices sapien consequat, varius massa. Nam auctor quam vel sapien convallis, at convallis felis faucibus. Ut vitae rutrum tortor, eget tempor ligula. Donec consequat faucibus libero, euismod varius nunc. Integer sapien dui, tincidunt id odio ac, gravida blandit metus. Proin varius sit amet nisl quis bibendum. Morbi sed nisl libero. Nam sagittis, leo ac viverra lobortis, quam diam laoreet enim, eu ullamcorper tellus sapien id est.In velit ante, dictum laoreet est et, suscipit euismod quam. Phasellus finibus pulvinar odio in pellentesque. Curabitur eu rhoncus sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque suscipit fermentum lacus, vitae scelerisque risus commodo at. Fusce viverra blandit lacus, eu mattis ipsum aliquam eu. Sed finibus urna lacinia tellus aliquet convallis. Nunc luctus dolor nisi, blandit faucibus nunc bibendum eu.Aliquam eu interdum velit, quis laoreet mi. Pellentesque eu tincidunt nunc. Aenean fermentum enim tellus, ut consequat velit efficitur sed. Maecenas erat enim, maximus eget commodo a, interdum mollis enim. Cras at scelerisque risus. Praesent fringilla sem a tortor pulvinar ultrices. Phasellus suscipit neque vitae velit vestibulum bibendum. Pellentesque molestie convallis velit, accumsan commodo nisi. Proin ac neque eleifend, cursus mauris nec, tempor nisl. Vestibulum ut tincidunt massa. Vivamus fermentum quam ut lorem sodales cursus. Vestibulum non massa ac nisi commodo fermentum. Suspendisse et sodales tortor. Pellentesque vestibulum lacus ut interdum sodales.Phasellus in dictum nulla. Phasellus bibendum laoreet magna eu sollicitudin. Nunc maximus velit neque, eu cursus orci egestas eu. Nunc sit amet consequat nisl, iaculis pulvinar mauris. Donec interdum eu sem sed congue. Vivamus scelerisque pulvinar pulvinar. Fusce at hendrerit ligula, nec molestie ante. Mauris commodo dictum lobortis. Quisque lacinia ornare est a rhoncus. Nam condimentum nisi ut dui blandit laoreet. Donec nec ultrices ante. Duis sodales vulputate viverra.Ut vestibulum libero eget quam pulvinar, vel feugiat mi laoreet. Ut congue lorem sed risus laoreet tincidunt. Sed varius sapien vel faucibus lobortis. Donec ut massa lacus. Cras eu dapibus justo. Fusce scelerisque mauris eros. Sed malesuada consectetur ligula vel auctor.'
send_data(message, packet_size)
