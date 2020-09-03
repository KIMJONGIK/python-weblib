from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# 인터넷에 localhost:8888
port = 8888

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):


        result = urlparse(self.path)


        if result.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('<h1>메인페이지입니다.</h1>'.encode('utf-8'))

        elif result.path == '/board':
            params = parse_qs(result.query)
            print(result.path)
            print(params)

            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('<h1>게시판입니다.</h1>'.encode('utf-8'))

        elif result.path == '/user':
            pass
        elif result.path == '/favicon, ico':
            pass



httpd = HTTPServer(('0.0.0.0', 8888), SimpleHTTPRequestHandler)
print(f'Server Running on Port {port}')
httpd.serve_forever()

# http://localhost:8888/board?a=list&p=1
# http://localhost:8888/board?a=list&p=1&p=2