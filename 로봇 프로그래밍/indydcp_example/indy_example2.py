from indy_utils import indydcp_client as client
import paho.mqtt.client as mqtt
from time import sleep

robot_ip = "192.168.3.2"
robot_name = "NRMK-Indy7"
indy = client.IndyDCPClient(robot_ip, robot_name)
indy.connect()

def motion_done_check():
    while True:
        status = indy.get_robot_status()
        if status['movedone'] == 1:
            print("motion Done")
            break
        sleep(0.1)

MQTT_BROKER = "192.168.3.63" #MQTT broker IP
MQTT_PORT = 1884; MQTT_TOPIC = "robot/command"

def on_connect(client, userdata, flags, rc):
    print("MQTT Connected");    client.subscribe(MQTT_TOPIC)
def on_message(client, userdata, msg):
    command = msg.payload.decode()
    print("MQTT Recieved: ", command)
    if command == "1":
        print("Robot Home 이동")
        indy.go_home(); motion_done_check()
    elif command == "2":
        print("Robot Zero 이동")
        indy.go_zero(); motion_done_check()

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect 
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 600)
print("Robot MQTT Control Start")

mqtt_client.loop_forever()
indy.disconnect()
