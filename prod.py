from confluent_kafka import Producer
#time is used to add delays between sending messages to simulate real-time data streaming.
import time

# Kafka configuration
bootstrap_servers = '172.28.48.1:29092'
topic_name = 'danske-topic1'

# Initialize the Kafka producer
producer = Producer({'bootstrap.servers': bootstrap_servers})

# Path to your .txt file
file_path = 'E:\ELK\logs.txt'

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced: {msg.value().decode('utf-8')}")

def send_file_to_kafka(file_path, topic_name):
    with open(file_path, 'r') as file:
        for line in file:
            # Send each line to the Kafka topic
            producer.produce(topic_name, value=line.encode('utf-8'), callback=acked)
            # Optional: Sleep to simulate real-time data streaming
            time.sleep(0.1)
            # Poll to handle delivery reports (callbacks)
           # producer.poll(0)
    producer.flush()
    print("Finished sending file to Kafka")

# Send the file to Kafka
send_file_to_kafka(file_path, topic_name)
