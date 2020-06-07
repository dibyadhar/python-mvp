#!/usr/bin/env python3
#
# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:8000 in your browser.

# Web servers using http.server are made of two parts: the HTTPServer class, 
# and a request handler class i.e BaseHTTPRequestHandler
from http.server import HTTPServer, BaseHTTPRequestHandler


class EchoHandler(BaseHTTPRequestHandler): # HelloHandler inherits BaseHTTPRequestHandler
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
    
        # Now, write the response body.
        message = self.path[1:]  # Extract 'bears' from '/bears', for instance
        message_bytes = message.encode()  # Make bytes from the string
        self.wfile.write(message_bytes)  # Send it over the network


if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, EchoHandler)
    httpd.serve_forever()
