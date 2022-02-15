from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import sys



class MyHTTPHandler(BaseHTTPRequestHandler):

    def handle_one_request(self):
        """Handle a single HTTP request.

        You normally don't need to override this method; see the class
        __doc__ string for information on how to handle specific HTTP
        commands such as GET and POST.

        """
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if len(self.raw_requestline) > 65536:
                self.requestline = ''
                self.request_version = ''
                self.command = ''
                self.send_error(HTTPStatus.REQUEST_URI_TOO_LONG)
                return
            if not self.raw_requestline:
                self.close_connection = True
                return
            if not self.parse_request():
                # An error code has been sent, just exit
                return

            #  ....................................................
            print(self.command, self.path)
            if self.command == 'GET':
                if self.path == '/':
                    self.send_response(HTTPStatus.OK)
                    self.send_header("Content-type", "text/html; charset=utf-8")
                    self.end_headers()

                    body = '''<h1>O Servidor tá ON!</h1>\n
                    <button>COMPRE!</button>
                    '''

                    self.wfile.write(body.encode('utf-8', 'replace'))

                elif self.path == '/blog':
                    self.send_response(HTTPStatus.PERMANENT_REDIRECT)
                    self.send_header('Location', 'https://henriquebastos.net/blog')
                    self.end_headers()

                elif self.path == '/api/order/1':
                    self.send_response(HTTPStatus.OK)
                    self.send_header("Content-type", "text/html; charset=utf-8")
                    self.end_headers()

                    body = '<h1>O Servidor tá ON!</h1>\n'

                    body = '{"id": 1, "product": "Café"}'
                    self.wfile.write(body.encode('utf-8', 'replace'))

            else:

                self.send_error(
                    HTTPStatus.NOT_IMPLEMENTED,
                    "Unsupported method (%r)" % self.command)
                return

            self.wfile.flush() #actually send the response if not already done.

        except socket.timeout as e:
            #a read or a write timed out.  Discard this connection
            self.log_error("Request timed out: %r", e)
            self.close_connection = True
            return


if __name__ == '__main__':
    # uma interface boba de linha de comando
    # inicia o seevidor
    # passa o nosso handler para ele
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', '-b', default='0.0.0.0')
    parser.add_argument('--port','-p', default=8000, type=int)
    args = parser.parse_args()

    with HTTPServer((args.bind, args.port), MyHTTPHandler) as httpd:
        host, port = httpd.socket.getsockname()[:2]
        url_host = f'[{host}]' if ':' in host else host

        print(f'Serving HTTP on {host} port {port} '
              f'(http://{url_host}:{port}/) ...'
        )

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nTchau!')
            sys.exit(0)