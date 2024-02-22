  CREATE TABLE if not exists default.events
  (
      event_ts  DateTime,
      user_id   Int32,
      operation String,
      status    Bool
  ) ENGINE = MergeTree
    ORDER BY event_ts;