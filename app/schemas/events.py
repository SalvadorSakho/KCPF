from sqlalchemy import String, Column, DATETIME, INTEGER, Boolean, DATE

from db.base_class import Base


class Events(Base):
    __tablename__ = "events"
    __schema_name__ = "default"

    events_date = Column('events_date', DATE, primary_key=True)
    event_ts = Column('event_ts', DATETIME)
    user_id = Column('user_id', INTEGER)
    operation = Column('operation', String)
    status = Column('status', Boolean)

