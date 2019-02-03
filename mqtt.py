from garage import Garage
import paho.mqtt.client as mqtt
import os
import sys

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    if rc == 0:
        print("Connection Accepted")
    elif rc == 1:
        print("The Server does not support "
                "the level of MQTT protocol "
                "requested by the Client")
    elif rc == 2:
        print("The client identifier is correct UTF-8 "
                "but not allowed by the Server")
    elif rc == 3:
        print("The Network Connection has been made "
                "but the MQTT service is unavailable")
    elif rc == 4:
        print("The data in the username or password "
                "is malformed")
    elif rc == 5:
        print("The client is not authorized to connect")

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("garage/activate")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic == "garage/activate":
        print("Message Recieved")
        print(msg.topic + " " + str(msg.payload))
        output_pin = int(os.environ["GARAGE_OUTPUT_PIN"])
        try:
            g = Garage(output_pin)
            g.activate()
            print("Garage activated")
        except:
            print("Unexpected error:", sys.exc_info()[0])
        finally:
            g.cleanup()
    else:
        print(f"Unhandled message topic: {msg.topic}, message: {msg.payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username=os.environ["MQTT_USERNAME"], password=os.environ["MQTT_PASSWD"])
client.connect("172.17.0.2", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
