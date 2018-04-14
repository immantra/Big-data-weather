import requests
from time import sleep
from kafka import KafkaProducer
import socket
from kafka import KafkaProducer
from CONSTANTS import *
import logging

# import ijson
import json

# filename = "city.list.json"
# f = open(filename, 'r',encoding="utf8")
# json_input= f.read()
# f.close()
# fichier = open('dataFichier.txt', 'w+',encoding="utf8")
#
#
#
# decoded = json.loads(json_input)
#
#     # Access data
# for x in decoded['cities']:
#     temp=x['id']
#     fichier.write(str(temp))
#     fichier.write('\n')
#     print (x['id'])
# fichier.close()



#enable logging
logging.basicConfig(level=logging.DEBUG)
def EnqueueStreamToKafkaTopic(data:str):

    producer.send(KAFKA_TOPIC, data)
    producer.flush()

print(KAFKA_ADDR)
producer = KafkaProducer(bootstrap_servers=KAFKA_ADDR, api_version=(0, 9), value_serializer=str.encode)
filedata = open('dataFichier.txt', 'r',encoding="utf8")
myKey= 'c927333e1812b2b48b7451bd75758f4c'
while True:
    print(filedata.readline())
    id = filedata.readline()
    id = id.strip('\n')
    param = {'id': id, 'APPID': myKey}
    r = requests.get(STREAM_HOST, params=param)
    data=r.json()
    print(data)
    if not data:
        print("ERROR")
        break
    else:
        print(data)
        EnqueueStreamToKafkaTopic(str(data))
        print('DONE!')
    sleep(3)


producer.close()
filedata.close()
print("END.")





