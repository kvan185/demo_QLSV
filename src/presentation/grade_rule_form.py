import tkinter as tk
from tkinter import ttk, messagebox

from src.business.grade_rule_service import get_grade_rules, add_or_update_rule
from src.business.course_service import get_all_courses


class GradeRuleFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.course_map = {}

        # ========== FORM ==========
        form = tk.Frame(self, padx=10, pady=10)
        form.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(form, text="Môn học").grid(row=0, column=0, sticky="w")
        self.cb_course = ttk.Combobox(form, state="readonly", width=30)
        self.cb_course.grid(row=0, column=1)

        tk.Label(form, text="Điểm tối thiểu").grid(row=1, column=0, sticky="w")
        self.entry_min = tk.Entry(form, width=20)
        self.entry_min.grid(row=1, column=1)

        tk.Label(form, text="Điểm đạt").grid(row=2, column=0, sticky="w")
        self.entry_pass = tk.Entry(form, width=20)
        self.entry_pass.grid(row=2, column=1)

        ttk.Button(form, text="Lưu", width=15, command=self.save).grid(
            row=3, column=1, pady=10
        )

        # ========== RIGHT ==========
        right = tk.Frame(self, padx=10, pady=10)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        search = tk.Frame(right)
        search.pack(fill=tk.X)

        tk.Label(search, text="Tìm kiếm").pack(side=tk.LEFT)
        self.entry_search = tk.Entry(search)
        self.entry_search.pack(side=tk.LEFT, padx=5)

        self.table = ttk.Treeview(
            right,
            columns=("course", "min", "pass"),
            show="headings"
        )

        self.table.heading("course", text="Môn học")
        self.table.heading("min", text="Điểm tối thiểu")
        self.table.heading("pass", text="Điểm đạt")

        self.table.column("course", width=200)
        self.table.column("min", width=100)
        self.table.column("pass", width=100)

        self.table.pack(fill=tk.BOTH, expand=True)

        # ========== EVENTS ==========
        self.entry_search.bind("<KeyRelease>", lambda e: self.load_table())
        self.table.bind("<<TreeviewSelect>>", self.on_select)

        self.load_courses()
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

    def load_table(self):
        self.table.delete(*self.table.get_children())
        for row in get_grade_rules(self.entry_search.get()):
            self.table.insert("", tk.END, values=row[:3])

    def on_select(self, event):
        selected = self.table.selection()
        if not selected:
            return

        course, min_s, pass_s = self.table.item(selected[0])["values"]

        self.cb_course.set(course)
        self.entry_min.delete(0, tk.END)
        self.entry_pass.delete(0, tk.END)

        self.entry_min.insert(0, min_s)
        self.entry_pass.insert(0, pass_s)

    def save(self):
        try:
            course_id = self.course_map[self.cb_course.get()]
            add_or_update_rule(
                course_id,
                float(self.entry_min.get()),
                float(self.entry_pass.get())
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã lưu quy định điểm")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
