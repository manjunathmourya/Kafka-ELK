✨ Kafka Commands

List kafka topics from the container


         docker exec -it kafka-cntr bash /bin/kafka-topics --list --bootstrap-server localhost:9092



Consume messages from the topic name 'danske-topic'


        docker exec -it kafka-cntr bash /bin/kafka-console-consumer --topic danske-topic --from-beginning --bootstrap-server localhost:9092


Produce messages via topic name 'codespotify-topic'


        docker exec -it kafka-cntr bash /bin/kafka-console-producer --topic danske-topic --bootstrap-server localhost:9092



Create topic if needed, logstash config handle the topic creation hence manual creation not required


        docker exec -it kafka-cntr bash /bin/kafka-topics --create --topic danske-topic --bootstrap-server localhost:9092


1. To view the indices 

           http://localhost:9200/_cat/indices




2. To ensure that each field has a consistent data type in Elasticsearch, you need to explicitly define a mapping for your Elasticsearch index. This will avoid dynamic mapping and ensure that fields are always indexed with the correct data type. Here is how you can create an index template in Elasticsearch and configure Logstash to use it.


- Using Kibana Dev Tools:
- Open Kibana.
- Go to Dev Tools.
- Enter the JSON payload and execute it.

PUT _index_template/your_index_template_name

{
  "index_patterns": ["logstash-*"],  // Pattern that matches your indices
  "template": {
    "settings": {
      "number_of_shards": 1,           // Number of primary shards
      "number_of_replicas": 1          // Number of replica shards
    },
    "mappings": {
      "properties": {
        "date": { "type": "date" },
        "time": { "type": "text" },
        "devname": { "type": "keyword" },
        "devid": { "type": "keyword" },
        "logid": { "type": "keyword" },
        "type": { "type": "keyword" },
        "subtype": { "type": "keyword" },
        "level": { "type": "keyword" },
        "vd": { "type": "keyword" },
        "eventtime": { "type": "long" },
        "srcip": { "type": "ip" },
        "srcport": { "type": "integer" },
        "srcintf": { "type": "keyword" },
        "srcintfrole": { "type": "keyword" },
        "dstip": { "type": "ip" },
        "dstport": { "type": "integer" },
        "dstintf": { "type": "keyword" },
        "dstintfrole": { "type": "keyword" },
        "poluuid": { "type": "keyword" },
        "sessionid": { "type": "long" },
        "proto": { "type": "integer" },
        "action": { "type": "keyword" },
        "policyid": { "type": "integer" },
        "policytype": { "type": "keyword" },
        "service": { "type": "keyword" },
        "dstcountry": { "type": "keyword" },
        "srccountry": { "type": "keyword" },
        "trandisp": { "type": "keyword" },
        "duration": { "type": "integer" },
        "sentbyte": { "type": "integer" },
        "rcvdbyte": { "type": "integer" },
        "sentpkt": { "type": "integer" },
        "appcat": { "type": "keyword" }
      }
    }
  }
}

6. To ensure that the index template was created successfully, you can check its details using the following in Kibana Dev Tools:

         GET /_index_template/danske_template


