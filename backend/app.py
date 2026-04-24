from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            response = b"Hello from Effective Mobile!"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Backend is running on port 8080")
    server.serve_forever()