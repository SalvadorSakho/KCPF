CREATE MATERIALIZED VIEW if not exists default.kafka_events_mv TO default.events AS
SELECT *
FROM default.kafka_events;