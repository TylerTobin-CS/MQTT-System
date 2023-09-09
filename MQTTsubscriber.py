# Tyler Tobin
# MQTT System
# SUBSCRIBER

import paho.mqtt.client as mqtt

# MQTT broker information
message_header = "example/topic"
broker = "mqtt://localhost:1883"
port = 1883


def connect(client, userdata, flags, rc):
    print("Connected: " + str(rc))
    client.subscribe(message_header)


def message(client, userdata, msg):
    print("Received message from: " + msg.message_header + ". Data: " + msg.payload.decode())



client = mqtt.Client("Subscriber")

client.on_connect = connect
client.on_message = message

client.connect(broker, port)

# Start client loop to listen for messages from publisher
client.loop_forever()