import tkinter as tk
import random

root = tk.Tk()
root.title("가짜 바이러스 폭주 시뮬레이션")
root.geometry("600x400")

canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

# 경고 텍스트
warning_text = canvas.create_text(300, 200, text="! 바이러스 감염 !", fill="red", font=("Arial", 30, "bold"))

# 화면 흔들기
def shake_window():
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    root.geometry(f"600x400+{300+x}+{200+y}")
    root.after(50, shake_window)

# 폭발 애니메이션
def explode():
    for _ in range(20):
        x = random.randint(0, 600)
        y = random.randint(0, 400)
        size = random.randint(5, 20)
        color = random.choice(["red", "orange", "yellow", "white"])
        canvas.create_oval(x-size, y-size, x+size, y+size, fill=color, outline="")
    canvas.after(200, explode)

# 시작 버튼
start_btn = tk.Button(root, text="펑! 시작", command=lambda: [shake_window(), explode()])
start_btn.pack(pady=10)

root.mainloop()
