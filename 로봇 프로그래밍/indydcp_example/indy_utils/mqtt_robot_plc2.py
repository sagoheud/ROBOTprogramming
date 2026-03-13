from indy_utils import indydcp_client as client
from pymcprotocol import Type3E
from time import sleep
import threading

ROBOT_IP = "192.168.3.2"
ROBOT_NAME = "NRMK-Indy7"

indy = client.IndyDCPClient(ROBOT_IP, ROBOT_NAME)
indy.connect()
print("Indy7 연결 성공")

PLC_IP = "192.168.3.20"
PLC_PORT = 1025

plc = Type3E()
plc.connect(PLC_IP, PLC_PORT)
print("PLC 연결 성공")

ADDR_START_ZERO = "M100"
ADDR_DONE_ZERO  = "M101"

ADDR_START_HOME = "M200"
ADDR_DONE_HOME  = "M201"

def motion_done_check():
    while True:
        status = indy.get_robot_status()
        if status["movedone"] == 1:
            break
        sleep(0.1)

def robot_motion(start_addr, done_addr, motion_func, motion_name):
    if plc.batchread_bitunits(start_addr, 1)[0] == 1:
        print(f"[PLC] {start_addr} 감지 -> {motion_name} 실행")
        motion_func()
        motion_done_check()
        print(f"[Robot] {motion_name} 완료")
        # Done ON
        plc.batchwrite_bitunits(done_addr, [1])
        print(f"[PLC] {motion_name} ON")
        sleep(1)
        # Done OFF
        plc.batchwrite_bitunits(done_addr, [0])
        print(f"[PLC] {motion_name} OFF")
        # Start OFF 대기
        while plc.batchread_bitunits(start_addr, 1)[0] ==1:
            sleep(0.1)
        print(f"[PLC] {start_addr} OFF 확인 -> 대기 상태")

def plc_monitor():
    while True:
        try:
            robot_motion(ADDR_START_ZERO, ADDR_DONE_ZERO, indy.go_zero, "Zero 이동")
            robot_motion(ADDR_START_HOME, ADDR_DONE_HOME, indy.go_home, "Home 이동")
            sleep(0.1)
        except Exception as e:
            print(f"[오류] PLC 감시 중 예외 발생: {e}")
            sleep(1)

try:
    plc_thread = threading.Thread(target=plc_monitor)
    plc_thread.start()
    plc_thread.join()   # 쓰레드 종료까지 대기

except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    indy.disconnect()
    plc.close()
    print("Indy7 및 PLC 연결 종료")  