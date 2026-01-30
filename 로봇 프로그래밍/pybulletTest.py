import pybullet as p
import pybullet_data
import time

# 물리 엔진 연결
physics_client = p.connect(p.GUI)  # GUI 모드 (p.DIRECT는 헤드리스 모드)
# 기본 데이터 경로 설정
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# 중력 설정
p.setGravity(0, 0, -9.81)

# 평면 로드
plane_id = p.loadURDF("plane.urdf")
# 객체 로드
cube_id = p.loadURDF("r2d2.urdf", [0, 0, 0.5])

# 시뮬레이션 실행
for i in range(10000):
    p.stepSimulation() 
    
    # 키보드 이벤트 확인
    keys = p.getKeyboardEvents()
    
    # 기본 속도 설정
    linear_vel = [0, 0, 0] # x, y, z 속도
    
    # 방향키 입력 처리 (상/하: X축, 좌/우: Y축)
    if p.B3G_UP_ARROW in keys and keys[p.B3G_UP_ARROW] & p.KEY_IS_DOWN:
        linear_vel[1] = 2  # 전진
    if p.B3G_DOWN_ARROW in keys and keys[p.B3G_DOWN_ARROW] & p.KEY_IS_DOWN:
        linear_vel[1] = -2 # 후진
    if p.B3G_LEFT_ARROW in keys and keys[p.B3G_LEFT_ARROW] & p.KEY_IS_DOWN:
        linear_vel[0] = -2  # 왼쪽
    if p.B3G_RIGHT_ARROW in keys and keys[p.B3G_RIGHT_ARROW] & p.KEY_IS_DOWN:
        linear_vel[0] = 2 # 오른쪽

    # 로봇에게 속도 적용
    p.resetBaseVelocity(cube_id, linearVelocity=linear_vel)
    time.sleep(1/240)
    
    if i % 240 == 0:
        pos, orn = p.getBasePositionAndOrientation(cube_id)
        print(f"Position: {pos}")

# 종료
p.disconnect()
