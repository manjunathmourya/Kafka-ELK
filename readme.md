✨ Kafka Commands

List kafka topics from the container
'''

         docker exec -it kafka-cntr bash /bin/kafka-topics --list --bootstrap-server localhost:9092

'''

Consume messages from the topic name 'danske-topic'
'''

        docker exec -it kafka-cntr bash /bin/kafka-console-consumer --topic danske-topic --from-beginning --bootstrap-server localhost:9092

'''
Produce messages via topic name 'codespotify-topic'
'''

        docker exec -it kafka-cntr bash /bin/kafka-console-producer --topic danske-topic --bootstrap-server localhost:9092

'''

Create topic if needed, logstash config handle the topic creation hence manual creation not required
'''

        docker exec -it kafka-cntr bash /bin/kafka-topics --create --topic danske-topic --bootstrap-server localhost:9092

'''