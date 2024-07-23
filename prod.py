from kafka import KafkaProducer
import time

# Kafka broker host and port
bootstrap_servers = '172.28.48.1:9092'  # Replace with your Kafka broker(s) bootstrap server

# Kafka topic to produce to
topic = 'codespotify-topic'  # Replace with your Kafka topic name

# Path to your text file
file_path = 'e:\ELK\logs.txt'  # Replace with the actual path to your .txt file

# Kafka producer configuration
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

def produce_file_contents(producer, file_path, topic):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Send each line as a message to Kafka
                producer.send(topic, line.encode('utf-8'))
                print(f"Producing: {line.strip()}")
                time.sleep(1)  # Adjust as needed to control message production rate

    except FileNotFoundError:
        print(f'Error: File {file_path} not found')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    # Produce file contents to Kafka
    produce_file_contents(producer, file_path, topic)
