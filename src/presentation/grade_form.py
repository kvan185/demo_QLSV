import tkinter as tk
from tkinter import ttk, messagebox
from src.business.grade_service import (
    get_grades,
    add_grade,
    edit_grade
)
from src.business.student_service import get_students
from src.business.course_service import get_courses


class GradeFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.student_map = {}
        self.course_map = {}
        self.selected_student = None
        self.selected_course = None

        # ================= LEFT FORM =================
        form = tk.Frame(self, padx=10, pady=10)
        form.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(form, text="Sinh viên").grid(row=0, column=0, sticky="w")
        self.cb_student = ttk.Combobox(form, state="readonly", width=28)
        self.cb_student.grid(row=0, column=1)

        tk.Label(form, text="Môn học").grid(row=1, column=0, sticky="w")
        self.cb_course = ttk.Combobox(form, state="readonly", width=28)
        self.cb_course.grid(row=1, column=1)

        tk.Label(form, text="Điểm").grid(row=2, column=0, sticky="w")
        self.entry_score = tk.Entry(form, width=30)
        self.entry_score.grid(row=2, column=1)

        ttk.Button(form, text="Thêm", width=15, command=self.add).grid(row=3, column=0, pady=10)
        ttk.Button(form, text="Cập nhật", width=15, command=self.update).grid(row=3, column=1)

        # ================= RIGHT =================
        right = tk.Frame(self, padx=10, pady=10)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # SEARCH
        search_frame = tk.Frame(right)
        search_frame.pack(fill=tk.X)

        tk.Label(search_frame, text="Tìm").pack(side=tk.LEFT)
        self.entry_search = tk.Entry(search_frame)
        self.entry_search.pack(side=tk.LEFT, padx=5)

        # SORT
        sort_frame = tk.Frame(right)
        sort_frame.pack(fill=tk.X, pady=5)

        tk.Label(sort_frame, text="ID SV").pack(side=tk.LEFT)
        self.cb_order = ttk.Combobox(
            sort_frame,
            values=["Tăng dần", "Giảm dần"],
            state="readonly",
            width=12
        )
        self.cb_order.current(0)
        self.cb_order.pack(side=tk.LEFT, padx=5)

        # TABLE
        self.table = ttk.Treeview(
            right,
            columns=("sid", "sname", "cname", "score"),
            show="headings"
        )

        self.table.heading("sid", text="ID SV")
        self.table.heading("sname", text="Sinh viên")
        self.table.heading("cname", text="Môn học")
        self.table.heading("score", text="Điểm")

        self.table.column("sid", width=70)
        self.table.column("sname", width=180)
        self.table.column("cname", width=160)
        self.table.column("score", width=60)

        self.table.pack(fill=tk.BOTH, expand=True)

        # EVENTS
        self.entry_search.bind("<KeyRelease>", lambda e: self.load_table())
        self.cb_order.bind("<<ComboboxSelected>>", lambda e: self.load_table())
        self.table.bind("<<TreeviewSelect>>", self.on_select)

        # INIT
        self.load_students()
        self.load_courses()
        self.load_table()

    # ================= LOGIC =================
    def load_students(self):
        values = []
        for sid, code, name, *_ in get_students():
            label = f"{name} (ID:{sid})"
            self.student_map[label] = sid
            values.append(label)
        self.cb_student["values"] = values
        if values:
            self.cb_student.current(0)

    def load_courses(self):
        values = []
        for cid, code, name, *_ in get_courses():
            label = f"{name} (ID:{cid})"
            self.course_map[label] = cid
            values.append(label)
        self.cb_course["values"] = values
        if values:
            self.cb_course.current(0)

    def load_table(self):
        keyword = self.entry_search.get()
        order = "ASC" if self.cb_order.get() == "Tăng dần" else "DESC"

        self.table.delete(*self.table.get_children())
        for g in get_grades(keyword, order):
            self.table.insert("", tk.END, values=g)

    def on_select(self, event):
        selected = self.table.selection()
        if not selected:
            return

        sid, sname, cname, score = self.table.item(selected[0])["values"]
        self.entry_score.delete(0, tk.END)
        self.entry_score.insert(0, score)

        for label, idv in self.student_map.items():
            if idv == sid:
                self.cb_student.set(label)

        for label, idv in self.course_map.items():
            if cname in label:
                self.cb_course.set(label)

        self.selected_student = sid
        self.selected_course = self.course_map[self.cb_course.get()]

    def add(self):
        try:
            add_grade(
                self.student_map[self.cb_student.get()],
                self.course_map[self.cb_course.get()],
                float(self.entry_score.get())
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã thêm điểm")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def update(self):
        if not self.selected_student or not self.selected_course:
            messagebox.showwarning("Chọn", "Chọn bản ghi cần cập nhật")
            return
        try:
            edit_grade(
                self.selected_student,
                self.selected_course,
                float(self.entry_score.get())
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã cập nhật điểm")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
