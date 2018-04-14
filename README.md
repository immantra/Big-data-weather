# Big-data-weather
terminal1:

cd Desktop/hadoop-cluster-docker/
docker start hadoop-master
docker start hadoop-slave1
docker start hadoop-slave2
docker exec -it hadoop-master bash
./start-kafka-zookeeper.sh 

terminal 2:

cd Desktop/hadoop-cluster-docker/
docker exec -it hadoop-master bash

terminal1:

kafka-console-consumer.sh --zookeeper localhost:2181 --topic Hello-Kafka --from-beginning

to test kafka use the next cmd on the terminal2:
kafka-console-producer.sh --broker-list 172.19.0.2:9092 --topic Hello-Kafka
then ctrl+c 

then run requette.py and you will get the json objectcts on terminal1


