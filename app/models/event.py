from datetime import datetime

from pydantic import BaseModel


class Event(BaseModel):
    event_ts: datetime
    user_id: int
    operation: str
    status: bool
