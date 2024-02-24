  CREATE TABLE if not exists default.events
  (
      events_date Date,
      event_ts  DateTime,
      user_id   Int32,
      operation String,
      status    Bool
  ) ENGINE = MergeTree
    ORDER BY events_date;