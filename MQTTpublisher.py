# Tyler Tobin
# MQTT System
# PUBLISHER

import paho.mqtt.client as mqtt

# MQTT Broker Information/setup
message_header = "PublishedBroadcast"
broker = "mqtt.eclipse.org"
port = 1883

client = mqtt.Client("Publisher")

client.connect(broker, port)
while True:
    message = input("Enter broadcast message: ")
    if message == "q":
        break
    else:
        continue
    client.publish(message_header, message)

client.disconnect()