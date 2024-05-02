import asyncio

from faststream.rabbit import RabbitBroker

from src.worker0 import Incoming


async def publish():
    async with RabbitBroker() as br:
        await br.publish(Incoming(m={'key2': 'value'}), "test")


asyncio.run(publish())
