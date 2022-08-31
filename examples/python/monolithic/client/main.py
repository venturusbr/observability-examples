import os
import logging
import uuid
import time
from datetime import datetime
from prometheus_client import start_http_server, Enum, Counter

EXPOSE_PORT = os.environ.get("EXPOSE_PORT", 8000)
LOG_PATH = '/var/log/client'

if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

logging.basicConfig(filename=f'{LOG_PATH}/main.log', level=logging.INFO)
logger = logging.getLogger(__name__)

enum = Enum('client_example_state', 'Client example state',
        states=['starting', 'running', 'stopped'])

counter = Counter('hello_said_count', 'How many times hello has been said')

log_id = str(uuid.uuid4())

start_http_server(8000)
enum.state('starting')
print('Starting...')
time.sleep(5)

logger.info(f"rid={log_id} system_started_at={datetime.now()} operation=Start")

try:
    while True:
        start_time = time.time()
        print(f'Hello world at {datetime.now()}')
        process_time = (time.time() - start_time) * 1000
        formatted_process_time = '{0:.2f}'.format(process_time)

        counter.inc(1)
        logger.info(f"rid={log_id} completed_in={formatted_process_time}ms operation=Hello")
        enum.state('running')
        time.sleep(5)
except KeyboardInterrupt:
    enum.state('stopped')
    print('Stopping...')
    time.sleep(5)
    logger.info(f"rid={log_id} system_stopped_at={datetime.now()} operation=Stop")