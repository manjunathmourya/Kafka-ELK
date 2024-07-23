from kafka import KafkaProducer

# Replace with your Kafka broker address
bootstrap_servers = '172.28.48.1:9092'
# Replace with your topic name
topic = "danske-topic"

# Open the text file in read mode
with open(".\logs.txt", "r") as file:
  producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
  # Read lines from the file
  for line in file:
      # Encode the line as bytes (optional, depending on message format)
      producer.send(topic, line.encode('utf-8'))
      print(f"Sent message: {line}")
  
  # Flush data to ensure all messages are sent
  producer.flush()

print("Finished sending messages")