from indy_utils import indydcp_client as client
import time
robot_ip = "192.168.3.2"
robot_name = "NRMK-Indy7"
indy = client.IndyDCPClient(robot_ip, robot_name)
indy.connect()
print("로봇 연결 성공")

def move_done_check():
    while True:
        if indy.get_robot_status()['movedone'] == 1:
            break
        time.sleep(0.1)

def generate_grid(base, grid_x, grid_y, offset_x, offset_y, layers=1, layer_h=0):
    coords = []
    for layer in range(layers):
        z = base[2] + layer * layer_h
        for i in range(grid_y):
            for j in range(grid_x):
                x = base[0] + j * offset_x
                y = base[1] + i * offset_y
                coords.append([x, y, z])
    return coords

# 작업1 : 2×2 Pick & Place
def task_pick2by2_place2by2():
    print("\n=== 작업1 시작 ===")

    PICK_BASE = [0.18605595778978153, 0.34356181695104195, 0.19940150110518265]
    PLACE_BASE = [0.06905595778978153, 0.22356181695104195, 0.19940150110518265]
    OFFSET_X = 0.04
    OFFSET_Y = 0.04
    RETRACT_Z = 0.05
    ROT_P = [-0.006518109219459515, -179.98968930569117, 120.2199313262332]
    ROT_R = [-0.006518109219459515, -179.98968930569117, 120.2199313262332]
    pick_positions = generate_grid(PICK_BASE, 2, 2, OFFSET_X, OFFSET_Y)
    place_positions = generate_grid(PLACE_BASE, 2, 2, OFFSET_X, OFFSET_Y)

    indy.go_home()
    move_done_check()

    for i in range(len(pick_positions)):
        pick = pick_positions[i]
        place = place_positions[i]
        print(f">> STEP {i+1}")

        # Pick
        indy.task_move_to([pick[0], pick[1], pick[2] + RETRACT_Z, *ROT_P])
        move_done_check()

        indy.task_move_to([pick[0], pick[1], pick[2], *ROT_P])
        move_done_check()

        indy.set_do(2, True)
        time.sleep(0.5)

        indy.task_move_to([pick[0], pick[1], pick[2] + RETRACT_Z, *ROT_P])
        move_done_check()

        # Place
        indy.task_move_to([place[0], place[1], place[2] + RETRACT_Z, *ROT_R])
        move_done_check()

        indy.task_move_to([place[0], place[1], place[2], *ROT_R])
        move_done_check()

        indy.set_do(2, False)
        time.sleep(0.5)

        indy.task_move_to([place[0], place[1], place[2] + RETRACT_Z, *ROT_R])
        move_done_check()

    indy.go_home()
    move_done_check()

    print("작업1 완료")

# 작업2 : 1×2 × 2단 팔레타이징
def task_pal_1by2_2layer():
    print("\n=== 작업2 시작 ===")

    PICK_BASE = [0.197853293248411, 0.494934342906699, 0.1533289339019412]
    PLACE_BASE = [0.11105595778978153, 0.26356181695104195, 0.19940150110518265]

    OFFSET_X = 0.04
    OFFSET_Y = 0.04
    LAYER_H = 0.03
    RETRACT_Z = 0.05

    ROT_P = [-22.51139089331165, -174.81963954473787, 66.80689867536479]
    ROT_R = [-0.006518109219459515, -179.98968930569117, 120.2199313262332]

    place_positions = generate_grid(
        PLACE_BASE,
        1,
        2,
        OFFSET_X,
        OFFSET_Y,
        layers=2,
        layer_h=LAYER_H
    )

    indy.go_home()
    move_done_check()

    for i, place in enumerate(place_positions):
        print(f">> STEP {i+1}")

        # Pick
        indy.task_move_to([PICK_BASE[0], PICK_BASE[1], PICK_BASE[2] + RETRACT_Z, *ROT_P])
        move_done_check()

        indy.task_move_to([PICK_BASE[0], PICK_BASE[1], PICK_BASE[2], *ROT_P])
        move_done_check()

        indy.set_do(2, True)
        time.sleep(0.5)

        indy.task_move_to([PICK_BASE[0], PICK_BASE[1], PICK_BASE[2] + RETRACT_Z, *ROT_P])
        move_done_check()

        # Place
        indy.task_move_to([place[0], place[1], place[2] + RETRACT_Z, *ROT_R])
        move_done_check()

        indy.task_move_to([place[0], place[1], place[2], *ROT_R])
        move_done_check()

        indy.set_do(2, False)
        time.sleep(0.5)

        indy.task_move_to([place[0], place[1], place[2] + RETRACT_Z, *ROT_R])
        move_done_check()
    indy.go_home()
    move_done_check()
    print("작업2 완료")

# 작업3 : 사용자 입력 팔레타이징
def task_custom_palletizing():
    print("\n=== 사용자 입력 팔레타이징 ===")
    try:
        line_count = int(input("한 줄에 몇 개 놓을 건가요? : "))
        total_count = int(input("총 몇 개를 놓을 건가요? : "))
    except:
        print("숫자를 입력하세요.")
        return

    PICK_BASE = [0.197853293248411, 0.494934342906699, 0.1533289339019412]
    PLACE_BASE = [0.11105595778978153, 0.26356181695104195, 0.19940150110518265]

    OFFSET_X = 0.04
    OFFSET_Y = 0.04
    RETRACT_Z = 0.05

    ROT_P = [-22.51139089331165, -174.81963954473787, 66.80689867536479]
    ROT_R = [-0.006518109219459515, -179.98968930569117, 120.2199313262332]

    place_positions = []

    for i in range(total_count):
        row = i // line_count
        col = i % line_count

        x = PLACE_BASE[0] + col * OFFSET_X
        y = PLACE_BASE[1] + row * OFFSET_Y
        z = PLACE_BASE[2]

        place_positions.append([x, y, z])

    indy.go_home()
    move_done_check()

    for i, place in enumerate(place_positions):
        print(f">> STEP {i+1}")

        indy.task_move_to([PICK_BASE[0], PICK_BASE[1], PICK_BASE[2] + RETRACT_Z, *ROT_P])
        move_done_check()

        indy.task_move_to([PICK_BASE[0], PICK_BASE[1], PICK_BASE[2], *ROT_P])
        move_done_check()

        indy.set_do(2, True)
        time.sleep(0.5)

        indy.task_move_to([PICK_BASE[0], PICK_BASE[1], PICK_BASE[2] + RETRACT_Z, *ROT_P])
        move_done_check()

        indy.task_move_to([place[0], place[1], place[2] + RETRACT_Z, *ROT_R])
        move_done_check()

        indy.task_move_to([place[0], place[1], place[2], *ROT_R])
        move_done_check()

        indy.set_do(2, False)
        time.sleep(0.5)

        indy.task_move_to([place[0], place[1], place[2] + RETRACT_Z, *ROT_R])
        move_done_check()

    indy.go_home()
    move_done_check()

    print("사용자 지정 팔레타이징 완료")

# 메인 실행부

print("\n=== 모드 선택 ===")
print("1 : 작업1 (2x2)")
print("2 : 작업2 (2단)")
print("3 : 사용자 입력 팔레타이징")

while True:
    keyboard_input = input("\n모드 입력 (1/2/3) : ")

    if keyboard_input == "1":
        task_pick2by2_place2by2()
    elif keyboard_input == "2":
        task_pal_1by2_2layer()
    elif keyboard_input == "3":
        task_custom_palletizing()
    time.sleep(0.1)