from sqlalchemy import String, Column, DATETIME, INTEGER, Boolean

from db.base_class import Base


class Events(Base):
    __tablename__ = "events"
    __schema_name__ = "default"

    event_ts = Column('event_ts', DATETIME, primary_key=True)
    user_id = Column('user_id', INTEGER)
    operation = Column('operation', String)
    status = Column('status', Boolean)

