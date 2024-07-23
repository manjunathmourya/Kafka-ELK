#!/bin/bash

# Replace with your Kafka broker and topic
BROKER_LIST="localhost:9092"
TOPIC="danske-topic"

# Input .txt file
INPUT_FILE="logs.txt"

# Check if the input file exists
if [ ! -f "$INPUT_FILE" ]; then
  echo "Error: Input file $INPUT_FILE not found."
  exit 1
fi

# Send each line of the file as a Kafka message
while IFS= read -r line; do
  kafka-console-producer \
    --broker-list $BROKER_LIST \
    --topic $TOPIC \
    --property "value.serializer=org.apache.kafka.common.serialization.StringSerializer" <<EOF
  $line
  EOF
done < "$INPUT_FILE"