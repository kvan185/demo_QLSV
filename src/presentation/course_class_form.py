import tkinter as tk
from tkinter import ttk, messagebox

from src.business.course_class_service import (
    add_course_class,
    edit_course_class,
    get_course_classes
)
from src.business.course_service import get_all_courses
from src.business.teacher_service import get_all_teachers


class CourseClassFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.selected_id = None
        self.course_map = {}
        self.teacher_map = {}

        # ========== FORM ==========
        form = tk.Frame(self, padx=10, pady=10)
        form.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(form, text="Môn học").grid(row=0, column=0, sticky="w")
        self.cb_course = ttk.Combobox(form, state="readonly", width=25)
        self.cb_course.grid(row=0, column=1)

        tk.Label(form, text="Giáo viên").grid(row=1, column=0, sticky="w")
        self.cb_teacher = ttk.Combobox(form, state="readonly", width=25)
        self.cb_teacher.grid(row=1, column=1)

        tk.Label(form, text="Học kỳ").grid(row=2, column=0, sticky="w")
        self.entry_semester = tk.Entry(form, width=25)
        self.entry_semester.grid(row=2, column=1)

        tk.Label(form, text="Năm học").grid(row=3, column=0, sticky="w")
        self.entry_year = tk.Entry(form, width=25)
        self.entry_year.grid(row=3, column=1)

        ttk.Button(form, text="Thêm", width=15, command=self.add).grid(row=4, column=0, pady=10)
        ttk.Button(form, text="Cập nhật", width=15, command=self.update).grid(row=4, column=1)

        # ========== RIGHT ==========
        right = tk.Frame(self, padx=10, pady=10)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        search = tk.Frame(right)
        search.pack(fill=tk.X)

        tk.Label(search, text="Tìm kiếm").pack(side=tk.LEFT)
        self.entry_search = tk.Entry(search)
        self.entry_search.pack(side=tk.LEFT, padx=5)

        self.cb_order = ttk.Combobox(
            search,
            values=["Tăng dần", "Giảm dần"],
            state="readonly",
            width=12
        )
        self.cb_order.current(0)
        self.cb_order.pack(side=tk.LEFT, padx=10)

        self.table = ttk.Treeview(
            right,
            columns=("id", "course", "teacher", "semester", "year"),
            show="headings"
        )

        for col, text, w in [
            ("id", "ID", 50),
            ("course", "Môn học", 150),
            ("teacher", "Giáo viên", 150),
            ("semester", "Học kỳ", 80),
            ("year", "Năm học", 100),
        ]:
            self.table.heading(col, text=text)
            self.table.column(col, width=w)

        self.table.pack(fill=tk.BOTH, expand=True)

        # ========== EVENTS ==========
        self.entry_search.bind("<KeyRelease>", lambda e: self.load_table())
        self.cb_order.bind("<<ComboboxSelected>>", lambda e: self.load_table())
        self.table.bind("<<TreeviewSelect>>", self.on_select)

        self.load_courses()
        self.load_teachers()
        self.load_table()

    # =====================
    def load_courses(self):
        values = []
        for cid, code, name, *_ in get_all_courses():
            label = f"{code} - {name}"
            self.course_map[label] = cid
            values.append(label)
        self.cb_course["values"] = values
        if values:
            self.cb_course.current(0)

    def load_teachers(self):
        values = []
        for tid, code, name in get_all_teachers():
            label = f"{code} - {name}"
            self.teacher_map[label] = tid
            values.append(label)
        self.cb_teacher["values"] = values
        if values:
            self.cb_teacher.current(0)

    def load_table(self):
        keyword = self.entry_search.get()
        order = "ASC" if self.cb_order.get() == "Tăng dần" else "DESC"

        self.table.delete(*self.table.get_children())
        for row in get_course_classes(keyword, order):
            self.table.insert("", tk.END, values=row)

    def on_select(self, event):
        selected = self.table.selection()
        if not selected:
            return

        data = self.table.item(selected[0])["values"]
        self.selected_id = data[0]

        self.entry_semester.delete(0, tk.END)
        self.entry_year.delete(0, tk.END)

        self.entry_semester.insert(0, data[3])
        self.entry_year.insert(0, data[4])

    def add(self):
        try:
            course_id = self.course_map[self.cb_course.get()]
            teacher_id = self.teacher_map[self.cb_teacher.get()]
            add_course_class(
                course_id,
                teacher_id,
                self.entry_semester.get(),
                self.entry_year.get()
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã thêm lớp học phần")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def update(self):
        try:
            course_id = self.course_map[self.cb_course.get()]
            teacher_id = self.teacher_map[self.cb_teacher.get()]
            edit_course_class(
                self.selected_id,
                course_id,
                teacher_id,
                self.entry_semester.get(),
                self.entry_year.get()
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã cập nhật lớp học phần")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
