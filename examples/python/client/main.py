from datetime import datetime
from time import sleep
from prometheus_client import start_http_server, Enum, Counter

enum = Enum('client_example_state', 'Client example state',
        states=['starting', 'running', 'stopped'])

counter = Counter('hello_said_count', 'How many times hello has been said')

start_http_server(8000)
enum.state('starting')
print('Starting...')
sleep(5)

try:
    while True:
        print(f'Hello world at {datetime.now()}')
        counter.inc(1)
        enum.state('running')
        sleep(5)
except KeyboardInterrupt:
    enum.state('stopped')
    print('Stopping...')
    sleep(5)