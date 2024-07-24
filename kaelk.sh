BROKER_LIST="172.28.48.1:29092"
TOPIC="danske_topic1"
FILE_PATH="E:\ELK\logs.txt"

# Send file contents to Kafka topic
cat $FILE_PATH | while read -r line
do
  echo "$line" | kafka-console-producer.sh --broker-list $BROKER_LIST --topic $TOPIC
  # Optional: Sleep to simulate real-time data streaming
  sleep 0.1
done

echo "Finished sending file to Kafka"