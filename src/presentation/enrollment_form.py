import tkinter as tk
from tkinter import ttk, messagebox
from src.business.enrollment_service import (
    add_enrollment,
    get_enrollments
)
from src.business.student_service import get_all_students
from src.business.class_service import get_all_course_classes


class EnrollmentFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # ===== FORM =====
        form = tk.Frame(self, padx=10, pady=10)
        form.pack(fill=tk.X)

        tk.Label(form, text="Sinh viên").grid(row=0, column=0)
        self.cb_student = ttk.Combobox(form, state="readonly", width=30)
        self.cb_student.grid(row=0, column=1)

        tk.Label(form, text="Lớp học phần").grid(row=1, column=0)
        self.cb_class = ttk.Combobox(form, state="readonly", width=30)
        self.cb_class.grid(row=1, column=1)

        ttk.Button(form, text="Đăng ký", command=self.add).grid(
            row=2, column=0, columnspan=2, pady=5
        )

        # ===== TABLE =====
        self.table = ttk.Treeview(
            self,
            columns=("student", "course", "semester", "year"),
            show="headings"
        )

        for col, text in [
            ("student", "Sinh viên"),
            ("course", "Môn học"),
            ("semester", "Học kỳ"),
            ("year", "Năm học")
        ]:
            self.table.heading(col, text=text)
            self.table.column(col, width=150)

        self.table.pack(fill=tk.BOTH, expand=True)

        # ===== DATA MAP =====
        self.student_map = {}
        self.class_map = {}

        self.load_students()
        self.load_classes()
        self.load_table()

    def load_students(self):
        values = []
        for sid, code, name, *_ in get_all_students():
            label = f"{code} - {name}"
            self.student_map[label] = sid
            values.append(label)
        self.cb_student["values"] = values
        if values:
            self.cb_student.current(0)

    def load_classes(self):
        values = []
        for cid, cname, semester, year in get_all_course_classes():
            label = f"{cname} ({semester}-{year})"
            self.class_map[label] = cid
            values.append(label)
        self.cb_class["values"] = values
        if values:
            self.cb_class.current(0)

    def load_table(self):
        self.table.delete(*self.table.get_children())
        for row in get_enrollments():
            self.table.insert("", tk.END, values=row)

    def add(self):
        try:
            student_id = self.student_map[self.cb_student.get()]
            class_id = self.class_map[self.cb_class.get()]
            add_enrollment(student_id, class_id)
            self.load_table()
            messagebox.showinfo("OK", "Đăng ký thành công")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
