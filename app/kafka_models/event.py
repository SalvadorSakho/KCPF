from faust import Record


class Event(Record):
    ts: int
    user_id: int
    operation: str
    status: bool

    def __str__(self):
        return (f"< Event timestamp: {self.ts}, user_id: {self.user_id}, operation: {self.operation},"
                f" status:{self.status}>")
