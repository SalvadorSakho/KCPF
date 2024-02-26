# KCPF

# Manual:
 - docker compose up - start all services.
 - open [kafka ui](http://localhost:8080/), and validate that topic **events** was successfully created 
 - run [add_kafka_events](https://github.com/SalvadorSakho/KCPF/blob/main/add_kafka_events.py) script, to produce events in kafka
 - use **kcpf endpoints** to check visualisation of data from clickhouse
   - Please use [Swagger](http://0.0.0.0:9090/docs#), to check available endpoints and those descriptions
