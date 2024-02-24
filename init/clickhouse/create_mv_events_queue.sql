CREATE MATERIALIZED VIEW if not exists default.kafka_events_mv TO default.events AS
SELECT
    toDate(event_ts) as events_date,
    toDateTime(event_ts) as event_ts,
    user_id,
    operation,
    status
FROM default.kafka_events;