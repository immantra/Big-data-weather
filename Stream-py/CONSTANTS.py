## Stream Parameters
STREAM_HOST = 'http://api.openweathermap.org/data/2.5/weather'
STREAM_PORT = 9999
STREAM_ADDR = (STREAM_HOST,STREAM_PORT)
STREAM_BUFSIZE = 4096

## Kafka Parameters

KAFKA_HOST = '172.19.0.2'
KAFKA_PORT = 9092
KAFKA_ADDR = KAFKA_HOST + ':' + str(KAFKA_PORT)
KAFKA_TOPIC = 'Hello-Kafka'
