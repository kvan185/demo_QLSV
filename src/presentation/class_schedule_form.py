import tkinter as tk
from tkinter import ttk, messagebox

from src.business.course_service import get_all_course_classes
from src.business.timetable_service import get_schedules, add_schedule

class ClassScheduleFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.course_class_map = {}

        # ================= LEFT FORM =================
        form = tk.Frame(self, padx=10, pady=10)
        form.pack(side=tk.LEFT, fill=tk.Y)

        # ---- Course class ----
        tk.Label(form, text="Lớp học phần").grid(row=0, column=0, sticky="w")
        self.cb_class = ttk.Combobox(form, state="readonly", width=35)
        self.cb_class.grid(row=0, column=1)

        # ---- Day ----
        tk.Label(form, text="Thứ").grid(row=1, column=0, sticky="w")
        self.cb_day = ttk.Combobox(
            form,
            values=["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7"],
            state="readonly",
            width=15
        )
        self.cb_day.current(0)
        self.cb_day.grid(row=1, column=1, sticky="w")

        # ---- Start period ----
        tk.Label(form, text="Tiết bắt đầu").grid(row=2, column=0, sticky="w")
        self.entry_start = tk.Entry(form, width=10)
        self.entry_start.grid(row=2, column=1, sticky="w")

        # ---- Periods ----
        tk.Label(form, text="Số tiết / buổi").grid(row=3, column=0, sticky="w")
        self.entry_periods = tk.Entry(form, width=10)
        self.entry_periods.grid(row=3, column=1, sticky="w")

        # ---- Room ----
        tk.Label(form, text="Phòng").grid(row=4, column=0, sticky="w")
        self.entry_room = tk.Entry(form, width=20)
        self.entry_room.grid(row=4, column=1, sticky="w")

        # ---- Total sessions ----
        tk.Label(form, text="Tổng số buổi").grid(row=5, column=0, sticky="w")
        self.entry_total = tk.Entry(form, width=10)
        self.entry_total.grid(row=5, column=1, sticky="w")

        ttk.Button(
            form,
            text="Thêm lịch",
            width=20,
            command=self.add_schedule
        ).grid(row=6, column=1, pady=10, sticky="w")

        # ================= RIGHT =================
        right = tk.Frame(self, padx=10, pady=10)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # ---- Table ----
        self.table = ttk.Treeview(
            right,
            columns=("day", "start", "periods", "room", "total"),
            show="headings"
        )

        self.table.heading("day", text="Thứ")
        self.table.heading("start", text="Tiết bắt đầu")
        self.table.heading("periods", text="Số tiết")
        self.table.heading("room", text="Phòng")
        self.table.heading("total", text="Tổng buổi")

        self.table.column("day", width=80)
        self.table.column("start", width=90)
        self.table.column("periods", width=80)
        self.table.column("room", width=100)
        self.table.column("total", width=80)

        self.table.pack(fill=tk.BOTH, expand=True)

        # ================= EVENTS =================
        self.cb_class.bind("<<ComboboxSelected>>", lambda e: self.load_table())

        self.load_course_classes()

    # ==================================================
    def load_course_classes(self):
        values = []
        for cid, course, semester, year in get_all_course_classes():
            label = f"{course} | {semester} | {year}"
            self.course_class_map[label] = cid
            values.append(label)

        self.cb_class["values"] = values
        if values:
            self.cb_class.current(0)
            self.load_table()

    def load_table(self):
        self.table.delete(*self.table.get_children())

        label = self.cb_class.get()
        if not label:
            return

        course_class_id = self.course_class_map[label]
        for day, start, periods, room, total in get_schedules(course_class_id):
            self.table.insert(
                "",
                tk.END,
                values=(self.day_text(day), start, periods, room, total)
            )

    def add_schedule(self):
        try:
            label = self.cb_class.get()
            if not label:
                raise ValueError("Chưa chọn lớp học phần")

            course_class_id = self.course_class_map[label]
            day = self.cb_day.current() + 2
            start = int(self.entry_start.get())
            periods = int(self.entry_periods.get())
            room = self.entry_room.get()
            total = int(self.entry_total.get())

            add_schedule(
                course_class_id,
                day,
                start,
                periods,
                room,
                total
            )

            self.load_table()
            messagebox.showinfo("OK", "Đã thêm lịch học")

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    @staticmethod
    def day_text(day):
        return {
            2: "Thứ 2",
            3: "Thứ 3",
            4: "Thứ 4",
            5: "Thứ 5",
            6: "Thứ 6",
            7: "Thứ 7"
        }.get(day, "")
