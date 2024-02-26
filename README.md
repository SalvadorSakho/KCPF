# KCPF

# Manual:
 - docker compose up - start all services.
 - open [kafka ui](http://localhost:8080/), and validate that topic **events** was successfully created 
 - run [add_kafka_events](https://github.com/SalvadorSakho/KCPF/blob/main/init/kafka/add_kafka_events.py) script, to produce events in kafka:
   - install python (version: 3.10)
   - install pip (version: 23.1.2)
   - using pip, install libs from requirements.txt file: pip install -r < path to [requirements.txt](https://github.com/SalvadorSakho/KCPF/blob/main/requirements.txt) file >
   - navigate to [add_kafka_events.py](https://github.com/SalvadorSakho/KCPF/blob/main/add_kafka_events.py) file: cd < path to file >
   - run command: python -m faust -A add_kafka_events worker -l info
 - use **kcpf endpoints** to check visualisation of data from clickhouse
   - Please use [Swagger](http://0.0.0.0:9090/docs#), to check available endpoints and those descriptions
