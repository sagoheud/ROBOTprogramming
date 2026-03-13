
from indy_utils import indydcp_client as client
import paho.mqtt.client as mqtt
import pymcprotocol
from time import sleep
import threading
# -----------------------------
# Robot 설정
# -----------------------------
robot_ip = "192.168.3.2"
robot_name = "NRMK-Indy7"

indy = client.IndyDCPClient(robot_ip, robot_name)
indy.connect()

# -----------------------------
# PLC 설정
# -----------------------------
plc = pymcprotocol.Type3E()

PLC_IP = "192.168.3.20"
PLC_PORT = 1025

plc.connect(PLC_IP, PLC_PORT)

print("PLC Connected")

# -----------------------------
# MQTT 설정
# -----------------------------
MQTT_BROKER = "192.168.3.63"
MQTT_PORT = 1884
MQTT_TOPIC = "robot/command123"

# -----------------------------
# Robot Motion Done Check
# -----------------------------
def motion_done_check():

    while True:
        status = indy.get_robot_status()

        if status['movedone'] == 1:
            print("Motion Done")
            break

        sleep(0.1)

# -----------------------------
# Robot Motion
# -----------------------------
def robot_home():

    print("Robot HOME 이동")

    indy.go_home()
    motion_done_check()

    plc.batchwrite_bitunits("M110", [1])
    sleep(0.5)
    plc.batchwrite_bitunits("M110", [0])

def robot_zero():

    print("Robot ZERO 이동")

    indy.go_zero()
    motion_done_check()

    plc.batchwrite_bitunits("M111", [1])
    sleep(0.5)
    plc.batchwrite_bitunits("M111", [0])

# -----------------------------
# MQTT 연결
# -----------------------------
def on_connect(client, userdata, flags, rc, properties=None):

    print("MQTT Connected")

    client.subscribe(MQTT_TOPIC)

# -----------------------------
# MQTT 메시지 수신
# -----------------------------
def on_message(client, userdata, msg):

    command = msg.payload.decode()

    print("MQTT Received :", command)

    if command == "1":
        robot_home()

    elif command == "2":
        robot_zero()

# -----------------------------
# MQTT Client
# -----------------------------
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 600)

# -----------------------------
# PLC Monitor
# -----------------------------
def plc_monitor():

    while True:

        home_start = plc.batchread_bitunits("M100", 1)[0]
        zero_start = plc.batchread_bitunits("M101", 1)[0]

        if home_start == 1:

            robot_home()
            plc.batchwrite_bitunits("M200", [1])

        if zero_start == 1:

            robot_zero()
            plc.batchwrite_bitunits("M201", [1])

        sleep(0.1)

# -----------------------------
# 프로그램 시작
# -----------------------------
print("Robot MQTT + PLC Control Start")

plc_thread = threading.Thread(target=plc_monitor)
plc_thread.start()

mqtt_client.loop_forever()

indy.disconnect()