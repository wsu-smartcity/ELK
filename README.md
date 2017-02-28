# ELK

## Python
This is a simple ftp client written in python. Simply modify the IP address and the username and password and it can be used to download any file from any ftp compatible device.

## Logstash
This is an example of what a logstash config file would look like. It makes use of grok to parse the incoming config files, which are in simple text format, into the json format that elasticsearch can then use. This particular grok pattern is designed to work with the SEL management box in our lab. The config files in that system have a simple pair value format of `"Config","value"`. The grok pattern can be modified to match any input format.
The input portion of the config file specifies what port logstash will use to receive data from. The output portion specifies the port on which the data will be forwarded to elasticsearch 
