import asyncio
import logging

from faststream import FastStream
from faststream.rabbit import RabbitBroker
from faststream.rabbit.annotations import RabbitMessage

import config
from models import GenericEvent, Status

broker = RabbitBroker(config.rabbit_url)

app = FastStream(broker)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Worker 1')


@broker.subscriber("event.1")
@broker.publisher("event.2")
async def process_event1(event: GenericEvent, msg: RabbitMessage):
    logger.info(f'Received event:\n{event}')
    await asyncio.sleep(10)
    # await msg.nack()
    return GenericEvent(
        event_name="event.2",
        status=Status.succeeded,
        data={
            'index': event.data['index']
        }
    )


if __name__ == "__main__":
    asyncio.run(app.run())
