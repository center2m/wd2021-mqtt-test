import paho.mqtt.client as mqtt
import logging
import config
import time
import json



def on_connect(client, userdata, flags, rc):
    log.info("Connected to MQTT with result code "+str(rc))
    #client.subscribe(f"application/{config.id_application}/device/+/event/up")

def on_message(client, userdata, msg):
    print(msg)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger("PUB_MQTT")


client = mqtt.Client(client_id=config.mqtt_id)
client.username_pw_set(config.mqtt_username, password=config.mqtt_pass)
#client.tls_set(ca_certs=config.mqtt_casert)
client.on_connect = on_connect
client.on_message = on_message

try:
    #client.connect(config.mqtt_host, config.mqtt_port, 60)
    client.connect_async(config.mqtt_host, config.mqtt_port, 60)
    client.loop_start()

    for i in range(4):
        time.sleep(70)
        pub= client.publish("wagon/hard0/test", payload=f"hello {i}", qos=0, retain=False)
        print(f"pub_res {pub.rc}")
except ConnectionRefusedError as e:
    log.exception(f'Connect to MQTT error: {e}')

#client.loop_forever()
