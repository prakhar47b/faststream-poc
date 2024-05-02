import asyncio
import logging

from fastapi import FastAPI
from faststream.rabbit import RabbitBroker
from faststream.rabbit.fastapi import RabbitRouter

import config
from models import GenericEvent, Status

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Worker 0')

router = RabbitRouter(config.rabbit_url, max_consumers=1, logger=logger)


@router.subscriber("event.0")
@router.publisher("event.1")
async def process_event0(event: GenericEvent):
    logger.info(f'Received event:\n{event}')
    await asyncio.sleep(5)
    return GenericEvent(
        event_name="event.1",
        status=Status.succeeded,
        data={
            'index': event.data['index']
        }
    )


@router.get("/start")
async def start_single():
    async with RabbitBroker(config.rabbit_url) as br:
        await br.publish(
            GenericEvent(
                event_name="event.0",
                status='SUCCEEDED',
                data={
                    'index': 0
                }
            ),
            queue='event.0'
        )
    return "OK"


@router.get("/bulk_start")
async def start_bulk():
    async with RabbitBroker(config.rabbit_url) as br:
        publish = [br.publish(
            GenericEvent(
                event_name="event.0",
                status=Status.succeeded,
                data={
                    'index': i
                }
            ),
            queue='event.0'
        ) for i in range(100)]
        await asyncio.gather(*publish)
    return "OK"


app = FastAPI(lifespan=router.lifespan_context)
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
