import http
import http.server
import cfgs

class MyHandler(http.server.SimpleHTTPRequestHandler):
    server_version = cfgs.local_settings["SERVER_VERSION"]
    
    def do_GET(self):
        self.send_response(http.HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, world!")

    def do_HEAD(self):
        self.send_response(http.HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()

def run(server_class=http.server.HTTPServer, handler_class=MyHandler, port=cfgs.local_settings["PORT"]):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down server")
        httpd.shutdown()

if __name__ == "__main__":
    run()

