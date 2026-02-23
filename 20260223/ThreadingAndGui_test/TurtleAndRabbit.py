import threading
import time

# 우승자를 기록할 리스트 (먼저 들어온 순서대로 쌓임)
finish_line = []

def turtle_run():
    print("거북이 출발")
    for i in range(1,21):
        time.sleep(0.9)
        print('거북이 -> %dm' %i)
    print('거북이 -> 20m 도착')
    finish_line.append("거북이") # 도착 시 리스트에 추가

def rabbit_run():
    print("토끼 출발")
    for i in range(1,14):
        time.sleep(0.35)
        print('토끼 -> %dm' %i)
    print('토끼 -> %dm 낮잠' %i)
    time.sleep(11)
    print('토끼 -> %dm 잠 깸' %i)
    for i in range(14,20):
        time.sleep(0.55)
        print('토끼 -> %dm' %i)
    print('토끼 -> 20m 도착')
    finish_line.append("토끼") # 도착 시 리스트에 추가

t1 = threading.Thread(target=turtle_run,daemon=True)
t2 = threading.Thread(target=rabbit_run,daemon=True)
t1.start()
t2.start()
t1.join()
t2.join()
# print("메인 스레드 종료 전 1초 대기...")
# time.sleep(1)
print("메인 스레드 종료 - (daemon=True 상태)")

# 결과 발표
# print("\n" + "="*20)
# print(f"우승자: {finish_line[0]}!!") # 리스트의 0번 인덱스가 무조건 1등
# print("="*20)