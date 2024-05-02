import asyncio
import logging

from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitQueue

import config
from models import GenericEvent, Status

broker = RabbitBroker(config.rabbit_url, max_consumers=1)

app = FastStream(broker)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Worker 2.0')


@broker.subscriber("event.2")
@broker.publisher("output")
async def process_event1(event: GenericEvent):
    logger.info(f'Received event:\n{event}')
    await asyncio.sleep(5)
    return GenericEvent(
        event_name="output2_0",
        status=Status.succeeded,
        data={
            'index': event.data['index']
        }
    )


async def main():
    await broker.connect()
    await broker.declare_queue(RabbitQueue('output'))
    await app.run()


if __name__ == "__main__":
    asyncio.run(main())
