import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------- 예시용 데이터/함수 ----------------
# 실제 데이터 파이프라인 구현 시 이 부분을 수정 필요
class DataPaths:
    """분석에 필요한 CSV 경로를 저장하는 클래스"""
    def __init__(self, samsung_card_csv, living_pop_csv, stores_csv, poi_csv):
        self.samsung_card_csv = samsung_card_csv
        self.living_pop_csv = living_pop_csv
        self.stores_csv = stores_csv
        self.poi_csv = poi_csv

class AnalysisConfig:
    """분석 설정값 저장 (필요시 확장 가능)"""
    pass

def run_pipeline(paths, cfg):
    """
    예시용 분석 파이프라인.
    실제 분석 로직을 여기에 연결 필요
    """
    # Top10 상권 예시 데이터
    top10 = pd.DataFrame({'상권': ['A','B','C'], '금액': [100, 200, 150]})
    # 시간대 패턴 예시 데이터
    hourly = pd.DataFrame({'시간대': ['10','11','12'], '건수': [10,20,15]})
    # 네트워크 엣지 예시 데이터
    network_edges = pd.DataFrame({'src':['A','B'], 'dst':['B','C'], 'weight':[0.5, 0.8]})
    # 상권 프로파일 예시 데이터
    area_profile = pd.DataFrame({'상권':['A','B'], '금액비중':[0.6,0.4], '건수비중':[0.7,0.3]})
    return {"top10": top10, "hourly": hourly, "network_edges": network_edges, "area_profile": area_profile}


# ---------------- GUI 코드 ----------------
class AnalysisApp:
    """대구 세대별 상권 분석용 GUI 클래스"""
    def __init__(self, root):
        self.root = root
        self.root.title("대구 세대별 상권 분석")
        self.root.configure(bg="#f0f4f8")  # 전체 배경색

        # ---------------- 파일 선택 UI 생성 ----------------
        self.create_file_selector("삼성카드 CSV:", 0, "sc_entry", self.select_samsung_card)
        self.create_file_selector("거주인구 CSV:", 1, "pop_entry", self.select_pop_csv)
        self.create_file_selector("상점 CSV:", 2, "store_entry", self.select_store_csv)
        self.create_file_selector("POI CSV:", 3, "poi_entry", self.select_poi_csv)

        # ---------------- 분석 실행 버튼 ----------------
        run_btn = tk.Button(root, text="분석 실행", command=self.run_analysis,
                            bg="#4a90e2", fg="white", font=("Arial", 12, "bold"),
                            padx=10, pady=5, activebackground="#357ABD", activeforeground="white")
        run_btn.grid(row=4, column=1, pady=15)

        # ---------------- 결과 텍스트박스 ----------------
        self.result_text = tk.Text(root, width=100, height=15, bg="#ffffff", fg="#333333", font=("Consolas", 10))
        self.result_text.grid(row=5, column=0, columnspan=3, pady=10, padx=10)

        # ---------------- 네트워크 시각화 영역 ----------------
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=3, pady=10)

    def create_file_selector(self, label_text, row, attr_name, command):
        """파일 선택 레이블 + 엔트리 + 버튼 생성"""
        # 레이블
        tk.Label(self.root, text=label_text, bg="#f0f4f8", fg="#333333", font=("Arial", 10, "bold"))\
            .grid(row=row, column=0, sticky="w", padx=10, pady=5)
        # 입력창
        entry = tk.Entry(self.root, width=50, bg="#ffffff", fg="#333333", font=("Arial", 10))
        entry.grid(row=row, column=1, padx=10)
        # 선택 버튼
        btn = tk.Button(self.root, text="선택", command=command, bg="#7ed6df", fg="#000000", padx=5,
                        activebackground="#4ecdc4")
        btn.grid(row=row, column=2, padx=5)
        setattr(self, attr_name, entry)  # 엔트리 객체를 클래스 속성으로 저장

    # ---------------- 파일 선택 이벤트 ----------------
    def select_samsung_card(self): self.select_file(self.sc_entry)
    def select_pop_csv(self): self.select_file(self.pop_entry)
    def select_store_csv(self): self.select_file(self.store_entry)
    def select_poi_csv(self): self.select_file(self.poi_entry)

    def select_file(self, entry_widget):
        """CSV 파일 선택 다이얼로그 실행"""
        path = filedialog.askopenfilename(filetypes=[("CSV 파일", "*.csv")])
        if path:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, path)

    # ---------------- 분석 실행 이벤트 ----------------
    def run_analysis(self):
        """
        분석 실행
        1. 입력 파일 경로 확인
        2. run_pipeline 호출
        3. 결과 텍스트 및 네트워크 시각화
        """
        try:
            # 파일 경로 객체 생성
            paths = DataPaths(
                samsung_card_csv=Path(self.sc_entry.get()),
                living_pop_csv=Path(self.pop_entry.get()),
                stores_csv=Path(self.store_entry.get()),
                poi_csv=Path(self.poi_entry.get())
            )
            cfg = AnalysisConfig()

            # 실제 분석 실행
            out = run_pipeline(paths, cfg)

            # ---------------- 결과 텍스트 출력 ----------------
            self.result_text.delete(1.0, tk.END)  # 기존 내용 초기화
            self.result_text.insert(tk.END, "Top10 상권 (세대별):\n", "title")
            self.result_text.insert(tk.END, str(out["top10"].head(10)) + "\n\n")
            self.result_text.insert(tk.END, "시간대 패턴 (세대별):\n", "title")
            self.result_text.insert(tk.END, str(out["hourly"].head(10)) + "\n\n")
            self.result_text.insert(tk.END, f"네트워크 엣지 수: {len(out['network_edges'])}\n", "title")
            self.result_text.insert(tk.END, "상권 프로파일 (세대별 금액/건수 비중):\n", "title")
            self.result_text.insert(tk.END, str(out["area_profile"].head(10)) + "\n\n")

            # 텍스트 제목 태그 스타일
            self.result_text.tag_config("title", foreground="#4a90e2", font=("Arial", 11, "bold"))

            # ---------------- 네트워크 시각화 ----------------
            self.ax.clear()
            G = nx.Graph()
            for _, row in out["network_edges"].iterrows():
                G.add_edge(row["src"], row["dst"], weight=row["weight"])

            pos = nx.spring_layout(G, seed=42)  # 위치 고정
            weights = [d["weight"] * 5 for _, _, d in G.edges(data=True)]
            nx.draw(G, pos, with_labels=True, node_color="#f6b93b",
                    edge_color="#95afc0", width=weights, ax=self.ax)
            self.ax.set_title("상권 공동 이용 네트워크", fontsize=12, color="#4a4a4a")
            self.canvas.draw()

        except Exception as e:
            # 오류 발생 시 메시지 박스
            messagebox.showerror("분석 오류", str(e))


# ---------------- 프로그램 실행 ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AnalysisApp(root)
    root.mainloop()
