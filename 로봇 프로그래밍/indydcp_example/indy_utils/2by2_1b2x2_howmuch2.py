import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from indy_utils import indydcp_client as client

# 테마 설정
THEME_BG = "#5A626C"  
LOG_BG = "#2F3136"    
STATUS_BG = "#1E1F22" 
TEXT_COLOR = "white"

class IndyControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Indy7 Advanced Control System")
        self.root.geometry("1200x850")
        self.root.configure(bg=THEME_BG)
        
        self.path_x, self.path_y, self.path_z = [], [], [] 
        self.points_x, self.points_y, self.points_z = [], [], [] 
        self.joint_labels = [] 
        
        self.robot_ip = "192.168.3.2"
        self.robot_name = "NRMK-Indy7"
        try:
            self.indy = client.IndyDCPClient(self.robot_ip, self.robot_name)
            self.indy.connect()
            self.is_connected = True
        except:
            self.is_connected = False
            print("로봇 연결 실패: 시뮬레이션 모드")

        self.setup_ui()
        self.update_status_loop()

    def setup_ui(self):
        # 1. 상단 버튼 프레임
        btn_frame = tk.Frame(self.root, bg=THEME_BG)
        btn_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        tk.Button(btn_frame, text="작업1 (2x2)", command=lambda: self.run_thread(self.task_1), width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="작업2 (2단)", command=lambda: self.run_thread(self.task_2), width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="작업3 (Custom)", command=lambda: self.run_thread(self.task_3), width=12).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="기록 삭제", command=self.clear_plots, bg="#FF6B6B", fg="white", width=10).pack(side=tk.RIGHT, padx=5)
        tk.Button(btn_frame, text="HOME", command=lambda: self.run_thread(self.go_home), bg="#FFA500", width=10).pack(side=tk.RIGHT, padx=5)

        # 2. 메인 바디
        body_frame = tk.Frame(self.root, bg=THEME_BG)
        body_frame.pack(fill=tk.BOTH, expand=True)

        # 로그 영역
        log_container = tk.Frame(body_frame, bg=THEME_BG)
        log_container.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)
        tk.Label(log_container, text="■ 로봇 동작 로그", bg=THEME_BG, fg=TEXT_COLOR, font=("맑은 고딕", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.log_area = scrolledtext.ScrolledText(log_container, width=40, height=30, bg=LOG_BG, fg=TEXT_COLOR, highlightthickness=0, borderwidth=0)
        self.log_area.pack(fill=tk.BOTH, expand=True)

        # 그래프 영역
        self.fig = plt.Figure(figsize=(5, 5), facecolor=THEME_BG)
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_facecolor(THEME_BG)
        self.ax.tick_params(colors=TEXT_COLOR)
        self.canvas = FigureCanvasTkAgg(self.fig, master=body_frame)
        self.canvas.get_tk_widget().config(bg=THEME_BG, highlightthickness=0)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # 3. 하단 조인트 상태바
        status_frame = tk.Frame(self.root, bg=STATUS_BG, height=70)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        tk.Label(status_frame, text="JOINT STATE", bg=STATUS_BG, fg="#888888", font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=15)

        for i in range(6):
            f = tk.Frame(status_frame, bg=STATUS_BG)
            f.pack(side=tk.LEFT, expand=True)
            tk.Label(f, text=f"J{i+1}", bg=STATUS_BG, fg="#00A8FF", font=("Arial", 9)).pack()
            val_label = tk.Label(f, text="0.00", bg=STATUS_BG, fg=TEXT_COLOR, font=("Consolas", 11, "bold"))
            val_label.pack()
            self.joint_labels.append(val_label)

        self.update_plot()

    def update_status_loop(self):
        if self.is_connected:
            try:
                j_pos = self.indy.get_joint_pos()
                for i in range(6): self.joint_labels[i].config(text=f"{j_pos[i]:.2f}")
            except: pass
        self.root.after(100, self.update_status_loop)

    def clear_plots(self):
        self.log_area.delete('1.0', tk.END)
        self.path_x, self.path_y, self.path_z = [], [], []
        self.points_x, self.points_y, self.points_z = [], [], []
        if self.is_connected:
            pos = self.indy.get_task_pos()
        else:
            pos = [0.3, 0.0, 0.5]

        self.path_x.append(pos[0])
        self.path_y.append(pos[1])
        self.path_z.append(pos[2])

        self.update_plot()
        self.log("기록이 초기화되었습니다.")

    def update_plot(self):
        self.ax.clear()
        if self.path_x:
            self.ax.plot(self.path_x, self.path_y, self.path_z, 'b-', alpha=0.4)
            self.ax.scatter(self.path_x[-1], self.path_y[-1], self.path_z[-1], color='black', s=80, zorder=5)
        if self.points_x:
            self.ax.scatter(self.points_x, self.points_y, self.points_z, color='red', s=40)
        self.ax.set_title("Real-time Simulation", color=TEXT_COLOR)
        self.canvas.draw()

    def log(self, msg):
        self.log_area.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {msg}\n")
        self.log_area.see(tk.END)

    def run_thread(self, func): Thread(target=func, daemon=True).start()

    def move_and_wait(self, pos, is_work_point=False):
        if self.is_connected:
            self.indy.task_move_to(pos)
            while self.indy.get_robot_status()['movedone'] == 0: time.sleep(0.05)
        else: time.sleep(0.1)
        p = pos[:3]
        if not self.path_x or ((self.path_x[-1]-p[0])**2 + (self.path_y[-1]-p[1])**2 + (self.path_z[-1]-p[2])**2)**0.5 > 0.001:
            self.path_x.append(p[0]); self.path_y.append(p[1]); self.path_z.append(p[2])
            if is_work_point: self.points_x.append(p[0]); self.points_y.append(p[1]); self.points_z.append(p[2])
        self.root.after(0, self.update_plot)

    def set_gripper(self, state):
        if self.is_connected: self.indy.set_do(2, state)
        self.log(f"Gripper: {'ON' if state else 'OFF'}")
        if self.path_x: self.points_x.append(self.path_x[-1]); self.points_y.append(self.path_y[-1]); self.points_z.append(self.path_z[-1])
        time.sleep(0.5)

    def go_home(self):
        self.log("홈으로 이동 중...")
        if self.is_connected:
            self.indy.go_home()
            while self.indy.get_robot_status()['movedone'] == 0: time.sleep(0.05)
            pos = self.indy.get_task_pos()
        else: pos = [0.3, 0.0, 0.5]
        if self.path_x:
            dist = ((self.path_x[-1]-pos[0])**2 + (self.path_y[-1]-pos[1])**2 + (self.path_z[-1]-pos[2])**2)**0.5
            if dist < 0.001:  # 1mm 미만 차이면 무시
                self.log("이미 홈 위치입니다.")
                return 
        # 중복이 아닐 때만 추가
        self.path_x.append(pos[0]); self.path_y.append(pos[1]); self.path_z.append(pos[2])
        self.update_plot()
        self.log("홈 이동 완료")

    # --- 작업 로직 ---
    def task_1(self):
        self.log("작업1(2x2) 시작")
        pb = [0.186, 0.343, 0.199]; pl = [0.069, 0.223, 0.199]
        rot = [-0.006, -179.98, 120.21]; rz = 0.05
        for i in range(4):
            curr_p = [pb[0]+(i%2)*0.04, pb[1]+(i//2)*0.04, pb[2]]
            curr_l = [pl[0]+(i%2)*0.04, pl[1]+(i//2)*0.04, pl[2]]
            self.move_and_wait([*curr_p[:2], curr_p[2]+rz, *rot])
            self.move_and_wait([*curr_p, *rot], True); self.set_gripper(True)
            self.move_and_wait([*curr_p[:2], curr_p[2]+rz, *rot])
            self.move_and_wait([*curr_l[:2], curr_l[2]+rz, *rot])
            self.move_and_wait([*curr_l, *rot], True); self.set_gripper(False)
            self.move_and_wait([*curr_l[:2], curr_l[2]+rz, *rot])
        self.go_home()

    def task_2(self):
        self.log("작업2(2단) 시작")
        pb = [0.197, 0.494, 0.153]; pl = [0.111, 0.263, 0.199]
        rp, rr = [-22.51, -174.81, 66.80], [-0.006, -179.98, 120.21]
        for i in range(4):
            z_off = (i//2)*0.03
            curr_l = [pl[0], pl[1]+(i%2)*0.04, pl[2]+z_off]
            self.move_and_wait([*pb[:2], pb[2]+0.05, *rp])
            self.move_and_wait([*pb, *rp], True); self.set_gripper(True)
            self.move_and_wait([*pb[:2], pb[2]+0.05, *rp])
            self.move_and_wait([*curr_l[:2], curr_l[2]+0.05, *rr])
            self.move_and_wait([*curr_l, *rr], True); self.set_gripper(False)
            self.move_and_wait([*curr_l[:2], curr_l[2]+0.05, *rr])
        self.go_home()

    def task_3(self):
        def submit():
            l, t = int(e1.get()), int(e2.get()); win.destroy()
            self.run_thread(lambda: self.execute_task_3(l, t))
        win = tk.Toplevel(self.root); win.title("Custom")
        tk.Label(win, text="가로:").grid(row=0, column=0); e1 = tk.Entry(win); e1.grid(row=0, column=1)
        tk.Label(win, text="총합:").grid(row=1, column=0); e2 = tk.Entry(win); e2.grid(row=1, column=1)
        tk.Button(win, text="시작", command=submit).grid(row=2, columnspan=2)

    def execute_task_3(self, ln, tc):
        pb, pl = [0.197, 0.494, 0.153], [0.111, 0.263, 0.199]
        rp, rr = [-22.51, -174.81, 66.80], [-0.006, -179.98, 120.21]
        for i in range(tc):
            curr_l = [pl[0]+(i%ln)*0.04, pl[1]+(i//ln)*0.04, pl[2]]
            self.move_and_wait([*pb[:2], pb[2]+0.05, *rp])
            self.move_and_wait([*pb, *rp], True); self.set_gripper(True)
            self.move_and_wait([*pb[:2], pb[2]+0.05, *rp])
            self.move_and_wait([*curr_l[:2], curr_l[2]+0.05, *rr])
            self.move_and_wait([*curr_l, *rr], True); self.set_gripper(False)
            self.move_and_wait([*curr_l[:2], curr_l[2]+0.05, *rr])
        self.go_home()

if __name__ == "__main__":
    root = tk.Tk(); app = IndyControlApp(root); root.mainloop()