import tkinter as tk
from tkinter import ttk, messagebox

from src.business.semester_service import (
    add_semester,
    edit_semester,
    get_semesters
)


class SemesterFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.selected_id = None

        # ========== FORM ==========
        form = tk.Frame(self, padx=10, pady=10)
        form.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(form, text="Tên học kỳ").grid(row=0, column=0, sticky="w")
        self.entry_name = tk.Entry(form, width=25)
        self.entry_name.grid(row=0, column=1)

        tk.Label(form, text="Ngày bắt đầu (YYYY-MM-DD)").grid(row=1, column=0, sticky="w")
        self.entry_start = tk.Entry(form, width=25)
        self.entry_start.grid(row=1, column=1)

        tk.Label(form, text="Ngày kết thúc (YYYY-MM-DD)").grid(row=2, column=0, sticky="w")
        self.entry_end = tk.Entry(form, width=25)
        self.entry_end.grid(row=2, column=1)

        ttk.Button(form, text="Thêm", width=15, command=self.add).grid(row=3, column=0, pady=10)
        ttk.Button(form, text="Cập nhật", width=15, command=self.update).grid(row=3, column=1)

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
            columns=("id", "name", "start", "end"),
            show="headings"
        )

        for col, text, w in [
            ("id", "ID", 50),
            ("name", "Tên học kỳ", 120),
            ("start", "Bắt đầu", 100),
            ("end", "Kết thúc", 100),
        ]:
            self.table.heading(col, text=text)
            self.table.column(col, width=w)

        self.table.pack(fill=tk.BOTH, expand=True)

        # ========== EVENTS ==========
        self.entry_search.bind("<KeyRelease>", lambda e: self.load_table())
        self.cb_order.bind("<<ComboboxSelected>>", lambda e: self.load_table())
        self.table.bind("<<TreeviewSelect>>", self.on_select)

        self.load_table()

    # =====================
    def load_table(self):
        keyword = self.entry_search.get()
        order = "ASC" if self.cb_order.get() == "Tăng dần" else "DESC"

        self.table.delete(*self.table.get_children())
        for row in get_semesters(keyword, order):
            self.table.insert("", tk.END, values=row)

    def on_select(self, event):
        selected = self.table.selection()
        if not selected:
            return

        data = self.table.item(selected[0])["values"]
        self.selected_id = data[0]

        self.entry_name.delete(0, tk.END)
        self.entry_start.delete(0, tk.END)
        self.entry_end.delete(0, tk.END)

        self.entry_name.insert(0, data[1])
        self.entry_start.insert(0, data[2])
        self.entry_end.insert(0, data[3])

    def add(self):
        try:
            add_semester(
                self.entry_name.get(),
                self.entry_start.get(),
                self.entry_end.get()
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã thêm học kỳ")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def update(self):
        try:
            edit_semester(
                self.selected_id,
                self.entry_name.get(),
                self.entry_start.get(),
                self.entry_end.get()
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã cập nhật học kỳ")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
