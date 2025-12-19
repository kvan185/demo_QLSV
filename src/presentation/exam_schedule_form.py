import tkinter as tk
from tkinter import ttk, messagebox
from src.business.course_service import get_all_course_classes
from src.business.timetable_service import get_exams, add_exam

class ExamScheduleFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.course_class_map = {}

        # ================= LEFT =================
        form = tk.Frame(self, padx=10, pady=10)
        form.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(form, text="Lớp học phần").grid(row=0, column=0, sticky="w")
        self.cb_class = ttk.Combobox(form, state="readonly", width=35)
        self.cb_class.grid(row=0, column=1)

        tk.Label(form, text="Ngày thi (YYYY-MM-DD)").grid(row=1, column=0, sticky="w")
        self.entry_date = tk.Entry(form, width=20)
        self.entry_date.grid(row=1, column=1)

        tk.Label(form, text="Giờ bắt đầu (HH:MM)").grid(row=2, column=0, sticky="w")
        self.entry_time = tk.Entry(form, width=20)
        self.entry_time.grid(row=2, column=1)

        tk.Label(form, text="Thời gian (phút)").grid(row=3, column=0, sticky="w")
        self.entry_duration = tk.Entry(form, width=20)
        self.entry_duration.grid(row=3, column=1)

        tk.Label(form, text="Phòng").grid(row=4, column=0, sticky="w")
        self.entry_room = tk.Entry(form, width=20)
        self.entry_room.grid(row=4, column=1)

        tk.Label(form, text="Hình thức").grid(row=5, column=0, sticky="w")
        self.cb_type = ttk.Combobox(
            form,
            values=["Giữa kỳ", "Cuối kỳ"],
            state="readonly",
            width=18
        )
        self.cb_type.current(0)
        self.cb_type.grid(row=5, column=1)

        ttk.Button(
            form,
            text="Thêm lịch thi",
            width=20,
            command=self.add_exam
        ).grid(row=6, column=1, pady=10)

        # ================= RIGHT =================
        right = tk.Frame(self, padx=10, pady=10)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.table = ttk.Treeview(
            right,
            columns=("date", "time", "duration", "room", "type"),
            show="headings"
        )

        for col, text, w in [
            ("date", "Ngày thi", 100),
            ("time", "Giờ", 80),
            ("duration", "Phút", 60),
            ("room", "Phòng", 100),
            ("type", "Hình thức", 80),
        ]:
            self.table.heading(col, text=text)
            self.table.column(col, width=w)

        self.table.pack(fill=tk.BOTH, expand=True)

        self.cb_class.bind("<<ComboboxSelected>>", lambda e: self.load_table())
        self.load_course_classes()

    # ====================================
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

        class_id = self.course_class_map[label]
        for row in get_exams(class_id):
            self.table.insert("", tk.END, values=row)

    def add_exam(self):
        try:
            label = self.cb_class.get()
            if not label:
                raise ValueError("Chưa chọn lớp học phần")

            add_exam(
                self.course_class_map[label],
                self.entry_date.get(),
                self.entry_time.get(),
                int(self.entry_duration.get()),
                self.entry_room.get(),
                self.cb_type.get()
            )

            self.load_table()
            messagebox.showinfo("OK", "Đã thêm lịch thi")

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
