import http.server
import random
import time
from prometheus_client import start_http_server, Counter, Summary, Histogram

REQUESTS = Counter("hello_worlds_total", "Hello Worlds requested via HTTP handler")
EXCEPTIONS = Counter("hello_worlds_exceptinos_total", "Hello Worlds failed via HTTP handler")
SALES = Counter("hello_world_sales_euro_total", "Euros made serving Hello World")

LATENCY = Summary('hello_world_latency_seconds',
        'Time for a request Hello World.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    @LATENCY.time()
    def do_GET(self):
        time.sleep(random.random() * 0.4)
        REQUESTS.inc()
        # with EXCEPTIONS.count_exceptions():
        #     if random.random() < 0.2:
        #         raise Exception
        SALES.inc(float(f'{(random.random() * 20):.2f}'))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello world, this is server written in Python!")

if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('127.0.0.1', 8001), MyHandler)
    server.serve_forever()
