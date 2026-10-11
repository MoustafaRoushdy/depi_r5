from flask import Flask
import time
from prometheus_client import start_http_server,  Counter , Gauge
app = Flask(__name__)
c = Counter('http_request', 'Total number of requests received')
g = Gauge('my_inprogress_requests', 'Requests current in progress')

@app.route('/')
def hello_world():
    c.inc()
    g.inc()
    time.sleep(30)
    g.dec()
    return 'Hello, K8S!'

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)
