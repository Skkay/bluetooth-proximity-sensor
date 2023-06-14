# Raspberry Pi Bluetooth Proximity Sensor

This Python script detects the presence of Bluetooth devices using a Raspberry Pi and publishes their status to an MQTT broker.

The main goal is to use it with Home Assistant as proximity sensor and add the presence status in some *automations*. Home Assistant configuration example at the end.

## Install

1. Install the required libraries using pip: `pip install -r requirements.txt`
2. Create the `config.yaml` file to configure the MQTT broker and the Bluetooth devices to scan for (check the template [config.yaml.dist](config.yaml.dist)).

## Usage

1. Run the script. The script will run forever in an infinite loop.
2. The status (`true` or `false`) of each device will be published to a topic in the format `<base_topic>/<device_slug>`.

### Run it through Docker

Be careful to select the correct OS architecture if you want to use it on a Raspberry Pi.

The image is also available on the Docker Hub: https://hub.docker.com/r/skkay/bluetooth-proximity-sensor.

A Docker Compose file is available here: [docker-compose.yml](docker-compose.yml).

## Configuration

The `config.yaml` file contains the following configuration options:

- `mqtt`:
  - `host`: The hostname or IP address of the MQTT broker.
  - `port`: The port number of the MQTT broker.
  - `base_topic`: The base topic to use for publishing device status.
- `devices`: A list of Bluetooth devices to scan for.
  - `mac`: The MAC address of the Bluetooth device.
  - `slug`: A device name, used as MQTT sub-topic.
- `scan_interval`: The interval between two scans, in seconds

## Home Assistant configuration example

MQTT binary sensor configuration:
```yaml
# configuration.yaml

mqtt:
  binary_sensor:
    - name: Bluetooth Presence - Honor BKL-L09
      state_topic: bluetooth-presence/honor-bkl-l09
      payload_on: 'true'
      payload_off: 'false'
```

Button configuration to show the device status:
```yaml
show_name: true
show_icon: true
type: button
tap_action:
  action: none
entity: binary_sensor.bluetooth_presence_honor_bkl_l09
show_state: true
```

Demo (`scan_interval` is set to `5`):

https://github.com/Skkay/bluetooth-proximity-sensor/assets/43747420/69c2b3c3-da8a-4e99-971a-9b786765013e.mp4
