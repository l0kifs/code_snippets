import logging
from http.server import BaseHTTPRequestHandler, HTTPServer


def run_server(self, port, url=''):
	class RequestHandler(BaseHTTPRequestHandler):
		# override log message format from BaseHTTPRequestHandler
		def log_message(self, format, *args):
			logging.info("%s - [%s] %s", self.address_string(), self.log_date_time_string(), format % args)

		def response(self):
			with open('index.html', 'rb') as file:
				self.wfile.write(file.read())

		def _set_headers(self):
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()

		def do_HEAD(self):
			self._set_headers()

		def do_GET(self):
			self._set_headers()
			self.response()

		def do_POST(self):
			request_path = self.path  # get request url path
			content_len = int(self.headers.get('Content-Length'))  # get POST request body length
			post_body = self.rfile.read(content_len)  # get POST request body according to length

			self._set_headers()
			self.response()

	server_address = (url, port)
	http_server = HTTPServer(server_address, RequestHandler)
	http_server.serve_forever()