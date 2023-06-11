import time
import bluetooth
import yaml
import paho.mqtt.client as mqtt

with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

mqttc = mqtt.Client()
mqttc.connect(config['mqtt']['host'], config['mqtt']['port'], 60)
mqttc.loop_start()

while True:
    for device in config['devices']:
        ping_res = bluetooth.lookup_name(device['mac'])

        mqtt_payload = 'true' if ping_res != None else 'false'
        mqtt_topic = config['mqtt']['base_topic'] + device['slug']

        print(f'Publishing to {mqtt_topic}: {mqtt_payload}')

        mqttc.publish(mqtt_topic, mqtt_payload)

    time.sleep(config['scan_interval'])
