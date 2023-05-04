from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        params = parse_qs(parsed_url.query)
        name = params.get('name', [''])[0]
        message = params.get('message', [''])[0]
        print('Received GET request:')
        print(f'Path: {parsed_url.path}')
        print(f'Query string: {parsed_url.query}')
        print(f'Params: {params}')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f'Hello {name}, {message}'.encode('cp1251'))


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f'Starting server on port {server_address[1]}')
    httpd.serve_forever()
