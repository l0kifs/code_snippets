import socket 
import ssl


def open_socket(self, hostname, port, secure=False):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	if secure:
		result_socket = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1_2, ciphers="ADH-AES128-SHA256")
	else:
		result_socket = sock

	result_socket.connect((hostname, port))
		
	return result_socket
