import uvicorn
import os
import logging
import uuid
import time
from typing import Union
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

EXPOSE_PORT = os.environ.get("EXPOSE_PORT", 8000)
LOG_PATH = '/var/log/fastapi'


if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

logging.basicConfig(filename=f'{LOG_PATH}/main.log', level=logging.INFO)
logger = logging.getLogger(__name__)

items_counter = Counter(
    "items_managed", "How many items calls were made", ["operation"]
)
hello_counter = Counter("hellos_said", "How many hellos have been said")


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class ItemResponse:
    id: int
    item_data: Item


items: dict[int, Item] = {}

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    EXCLUDED_PATHS_FROM_LOG = ['/metrics']
    log_id = str(uuid.uuid4())
    if request.url.path not in EXCLUDED_PATHS_FROM_LOG:
        logger.info(f"rid={log_id} start request path={request.url.path}") 
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    if request.url.path not in EXCLUDED_PATHS_FROM_LOG:
        logger.info(f"rid={log_id} completed_in={formatted_process_time}ms status_code={response.status_code}")
    
    return response


@app.get("/hello")
def read_root():
    hello_counter.inc(1)
    return {"Hello": "World"}


@app.post("/items/{item_id}")
def write_item(item_id: int, item: Item):
    items_counter.labels("add").inc(1)
    items[item_id] = item
    response = ItemResponse()
    response.id = item_id
    response.item_data = item
    return response


@app.get("/items")
def read_items():
    items_counter.labels("list").inc(1)
    return items


@app.get("/items/{item_id}")
def read_item(item_id: int):
    items_counter.labels("look").inc(1)
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return items[item_id]


Instrumentator().instrument(app).expose(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=EXPOSE_PORT)
