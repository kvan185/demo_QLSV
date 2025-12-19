import tkinter as tk
from tkinter import ttk, messagebox
from src.business.timetable_service import get_week_timetable
from src.business.student_service import fetch_all_students

class TimetableFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.student_map = {}
        self.max_periods = 10

        # ========== TOP ==========
        top = tk.Frame(self, padx=10, pady=5)
        top.pack(fill=tk.X)

        tk.Label(top, text="Sinh viên").pack(side=tk.LEFT)
        self.cb_student = ttk.Combobox(top, state="readonly", width=30)
        self.cb_student.pack(side=tk.LEFT, padx=5)

        ttk.Button(top, text="Xem TKB", command=self.load_timetable).pack(side=tk.LEFT)

        # ========== TABLE ==========
        self.table = tk.Frame(self)
        self.table.pack(padx=10, pady=10)

        self.load_students()
        self.draw_header()

    # =============================
    def load_students(self):
        values = []
        for sid, code, name, *_ in fetch_all_students():
            label = f"{code} - {name}"
            self.student_map[label] = sid
            values.append(label)

        self.cb_student["values"] = values
        if values:
            self.cb_student.current(0)

    def draw_header(self):
        tk.Label(self.table, text="Thứ / Tiết", width=12, borderwidth=1, relief="solid").grid(row=0, column=0)

        for p in range(1, self.max_periods + 1):
            tk.Label(
                self.table,
                text=f"Tiết {p}",
                width=12,
                borderwidth=1,
                relief="solid"
            ).grid(row=0, column=p)

    def load_timetable(self):
        if not self.cb_student.get():
            messagebox.showwarning("Chú ý", "Chọn sinh viên")
            return

        student_id = self.student_map[self.cb_student.get()]
        data = get_week_timetable(student_id, self.max_periods)

        # Clear cũ
        for widget in self.table.winfo_children():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()

        # Vẽ bảng
        row = 1
        for day in range(2, 8):
            tk.Label(
                self.table,
                text=f"Thứ {day}",
                width=12,
                borderwidth=1,
                relief="solid"
            ).grid(row=row, column=0)

            for p in range(1, self.max_periods + 1):
                tk.Label(
                    self.table,
                    text=data[day][p],
                    width=12,
                    height=3,
                    borderwidth=1,
                    relief="solid",
                    wraplength=90,
                    justify="center"
                ).grid(row=row, column=p)

            row += 1
