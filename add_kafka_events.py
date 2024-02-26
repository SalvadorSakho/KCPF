import os

import faust
from faust import Record
from random import randint, randrange
from datetime import datetime, timedelta


class Event(Record):
    event_ts: int
    user_id: int
    operation: str
    status: bool

    def __str__(self):
        return (f"< Event timestamp: {self.event_ts}, user_id: {self.user_id}, operation: {self.operation},"
                f" status:{self.status}>")


# defining consumer group by: id, broker address, event structure type
app = faust.App('myKafkaApp', broker='localhost:9092', value_serializer='json')
events_topic = app.topic('events', value_type=Event)


def random_datetime(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


@app.task
async def example_sender(app):
    msg_qty = 1000
    while msg_qty > 0:
        operation_type = ['like', 'dislike', 'kiss', 'surprised', 'dissatisfied'][randint(0, 4)]
        random_dt = random_datetime(datetime(2023, 1, 1), datetime(2024, 2, 28))
        kafka_event_ts = int(random_dt.timestamp())
        event = Event(
            event_ts=kafka_event_ts,
            user_id=randint(1, 200),
            operation=operation_type,
            status=[True, False][randint(0, 1)]
        )
        print(f'{event}')
        await events_topic.send(key=str(kafka_event_ts), value=event)
        msg_qty -= 1
    print('Finished to generate kafka data')
    os._exit(1)

if __name__ == '__main__':
    app.main()
