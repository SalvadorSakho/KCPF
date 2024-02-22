import faust
from random import randint
from datetime import datetime
from utils.project_logger import logger

from kafka_models.event import Event
from configs.config import KAFKA_URL

app = faust.App('myKafkaApp',
                broker=KAFKA_URL,
                value_serializer='json')

events_topic = app.topic('events', value_type=Event)


@app.agent(events_topic, concurrency=3)
async def events_topic(events):
    async for events_list in events.take(10000, within=10):
        logger.info(f'{events.shortlabel} - start processing part: {events_list[0].ts}')
        for order in events_list:
            logger.info(f'{order}')
        logger.info(f'{events.shortlabel} - finished processing part: {events_list[0].ts}')


@app.timer(interval=2.0)
async def example_sender(app):
    operation_type = ['like', 'dislike', 'kiss', 'surprised', 'dissatisfied'][randint(0, 4)]
    kafka_event_key = datetime.now()
    event = Event(
        ts=kafka_event_key,
        user_id=randint(1, 200),
        operation=operation_type,
        status=[True, False][randint(0, 1)]
    )
    await events_topic.send(key=str(int(kafka_event_key.timestamp())), value=event)


if __name__ == '__main__':
    app.main()
