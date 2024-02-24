from datetime import datetime, date

from pydantic import BaseModel


class Event(BaseModel):
    events_date: date
    event_ts: datetime
    user_id: int
    operation: str
    status: bool
