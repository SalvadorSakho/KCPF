CREATE TABLE if not exists default.kafka_events
(
    event_ts  Int32,
    user_id   Int32,
    operation String,
    status    Bool
) ENGINE = Kafka('kafka:9099', 'events', 'events_kafka_group', 'JSONEachRow')
SETTINGS
    kafka_num_consumers = 3
-- 3 = kafka_num_consumers = kafka topic partitions qty