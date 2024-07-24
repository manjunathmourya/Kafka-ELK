1. To view the indices 

     http://localhost:9200/_cat/indices

2. https://chatgpt.com/c/24a7c138-7b46-4a92-9300-dba0c7321c80 -- filter
3. https://chatgpt.com/c/e1e9bb46-98fb-4298-9d38-bd6e3d1058b1 -- python script


4. To ensure that each field has a consistent data type in Elasticsearch, you need to explicitly define a mapping for your Elasticsearch index. This will avoid dynamic mapping and ensure that fields are always indexed with the correct data type. Here is how you can create an index template in Elasticsearch and configure Logstash to use it.


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

5. To ensure that the index template was created successfully, you can check its details using the following in Kibana Dev Tools:

         GET /_index_template/danske_template
