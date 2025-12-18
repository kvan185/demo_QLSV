import tkinter as tk
from tkinter import ttk, messagebox

from src.business.teacher_service import (
    add_teacher,
    edit_teacher,
    get_teachers,
    get_all_teachers
)


class TeacherFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.selected_id = None

        # ================= LEFT FORM =================
        form = tk.Frame(self, padx=10, pady=10)
        form.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(form, text="Mã GV").grid(row=0, column=0, sticky="w")
        self.entry_code = tk.Entry(form, width=25)
        self.entry_code.grid(row=0, column=1)

        tk.Label(form, text="Họ tên").grid(row=1, column=0, sticky="w")
        self.entry_name = tk.Entry(form, width=25)
        self.entry_name.grid(row=1, column=1)

        tk.Label(form, text="Học vị").grid(row=2, column=0, sticky="w")
        self.entry_degree = tk.Entry(form, width=25)
        self.entry_degree.grid(row=2, column=1)

        ttk.Button(form, text="Thêm", width=15, command=self.add).grid(
            row=3, column=0, pady=10
        )
        ttk.Button(form, text="Cập nhật", width=15, command=self.update).grid(
            row=3, column=1
        )

        # ================= RIGHT =================
        right = tk.Frame(self, padx=10, pady=10)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # ---------- SEARCH ----------
        search_frame = tk.Frame(right)
        search_frame.pack(fill=tk.X)

        tk.Label(search_frame, text="Tìm kiếm").pack(side=tk.LEFT)
        self.entry_search = tk.Entry(search_frame)
        self.entry_search.pack(side=tk.LEFT, padx=5)

        tk.Label(search_frame, text="ID").pack(side=tk.LEFT, padx=10)
        self.cb_order = ttk.Combobox(
            search_frame,
            values=["Tăng dần", "Giảm dần"],
            state="readonly",
            width=12
        )
        self.cb_order.current(0)
        self.cb_order.pack(side=tk.LEFT)

        # ---------- TABLE ----------
        self.table = ttk.Treeview(
            right,
            columns=("id", "code", "name", "degree"),
            show="headings"
        )

        for col, text, w in [
            ("id", "ID", 60),
            ("code", "Mã GV", 100),
            ("name", "Họ tên", 180),
            ("degree", "Học vị", 100),
        ]:
            self.table.heading(col, text=text)
            self.table.column(col, width=w)

        self.table.pack(fill=tk.BOTH, expand=True)

        # ================= EVENTS =================
        self.entry_search.bind("<KeyRelease>", lambda e: self.load_table())
        self.cb_order.bind("<<ComboboxSelected>>", lambda e: self.load_table())
        self.table.bind("<<TreeviewSelect>>", self.on_select)

        self.load_table()

    # ================= LOGIC =================
    def load_table(self):
        keyword = self.entry_search.get()
        order = "ASC" if self.cb_order.get() == "Tăng dần" else "DESC"

        self.table.delete(*self.table.get_children())
        for t in get_teachers(keyword, order):
            self.table.insert("", tk.END, values=t)

    def on_select(self, event):
        selected = self.table.selection()
        if not selected:
            return

        data = self.table.item(selected[0])["values"]
        self.selected_id = data[0]

        self.entry_code.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_degree.delete(0, tk.END)

        self.entry_code.insert(0, data[1])
        self.entry_name.insert(0, data[2])
        self.entry_degree.insert(0, data[3])

    def add(self):
        try:
            add_teacher(
                self.entry_code.get(),
                self.entry_name.get(),
                self.entry_degree.get()
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã thêm giáo viên")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def update(self):
        try:
            edit_teacher(
                self.selected_id,
                self.entry_code.get(),
                self.entry_name.get(),
                self.entry_degree.get()
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã cập nhật giáo viên")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
