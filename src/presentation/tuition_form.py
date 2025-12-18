import tkinter as tk
from tkinter import ttk, messagebox

from src.business.tuition_service import (
    get_tuition_settings,
    get_course_fee
)
from src.business.course_service import get_all_courses


class TuitionFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.course_map = {}
        self.system_map = {}

        # ===== FORM =====
        form = tk.Frame(self, padx=10, pady=10)
        form.pack()

        tk.Label(form, text="Môn học").grid(row=0, column=0)
        self.cb_course = ttk.Combobox(form, width=30, state="readonly")
        self.cb_course.grid(row=0, column=1)

        tk.Label(form, text="Hệ đào tạo").grid(row=1, column=0)
        self.cb_system = ttk.Combobox(form, width=30, state="readonly")
        self.cb_system.grid(row=1, column=1)

        ttk.Button(form, text="Tính học phí", command=self.calculate).grid(
            row=2, column=1, pady=10
        )

        self.lbl_result = tk.Label(form, text="", font=("Arial", 12, "bold"))
        self.lbl_result.grid(row=3, column=0, columnspan=2)

        self.load_data()

    def load_data(self):
        courses = []
        for cid, code, name, credit in get_all_courses():
            label = f"{code} - {name} ({credit} TC)"
            self.course_map[label] = cid
            courses.append(label)
        self.cb_course["values"] = courses
        self.cb_course.current(0)

        systems = []
        for sid, name, price, coef in get_tuition_settings():
            label = f"{name} (x{coef})"
            self.system_map[label] = sid
            systems.append(label)
        self.cb_system["values"] = systems
        self.cb_system.current(0)

    def calculate(self):
        try:
            course_id = self.course_map[self.cb_course.get()]
            system_id = self.system_map[self.cb_system.get()]
            fee = get_course_fee(course_id, system_id)
            self.lbl_result.config(
                text=f"Học phí môn: {fee:,.0f} VNĐ"
            )
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
