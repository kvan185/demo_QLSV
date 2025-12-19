import tkinter as tk
from tkinter import ttk, messagebox
from src.business.course_service import  get_courses, add_course, edit_course

class CourseFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.selected_id = None

        # ================= LEFT FORM =================
        form = tk.Frame(self, padx=10, pady=10)
        form.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(form, text="Mã môn").grid(row=0, column=0, sticky="w")
        self.entry_code = tk.Entry(form, width=25)
        self.entry_code.grid(row=0, column=1)

        tk.Label(form, text="Tên môn").grid(row=1, column=0, sticky="w")
        self.entry_name = tk.Entry(form, width=25)
        self.entry_name.grid(row=1, column=1)

        tk.Label(form, text="Số tín chỉ").grid(row=2, column=0, sticky="w")
        self.entry_credit = tk.Entry(form, width=25)
        self.entry_credit.grid(row=2, column=1)

        ttk.Button(form, text="Thêm", width=15, command=self.add).grid(row=3, column=0, pady=10)
        ttk.Button(form, text="Cập nhật", width=15, command=self.update).grid(row=3, column=1)

        # ================= RIGHT SIDE =================
        right = tk.Frame(self, padx=10, pady=10)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # ---------- SEARCH ----------
        search_frame = tk.Frame(right)
        search_frame.pack(fill=tk.X)

        tk.Label(search_frame, text="Tìm kiếm").pack(side=tk.LEFT)
        self.entry_search = tk.Entry(search_frame)
        self.entry_search.pack(side=tk.LEFT, padx=5)

        # ---------- FILTER ----------
        filter_frame = tk.Frame(right)
        filter_frame.pack(fill=tk.X, pady=5)

        tk.Label(filter_frame, text="ID").pack(side=tk.LEFT)
        self.cb_order = ttk.Combobox(
            filter_frame,
            values=["Tăng dần", "Giảm dần"],
            state="readonly",
            width=12
        )
        self.cb_order.current(0)
        self.cb_order.pack(side=tk.LEFT, padx=5)

        # ---------- TABLE ----------
        self.table = ttk.Treeview(
            right,
            columns=("id", "code", "name", "credit"),
            show="headings"
        )

        self.table.heading("id", text="ID")
        self.table.heading("code", text="Mã môn")
        self.table.heading("name", text="Tên môn")
        self.table.heading("credit", text="Tín chỉ")

        self.table.column("id", width=60)
        self.table.column("code", width=100)
        self.table.column("name", width=200)
        self.table.column("credit", width=80)

        self.table.pack(fill=tk.BOTH, expand=True)

        # ================= EVENTS =================
        self.entry_search.bind("<KeyRelease>", lambda e: self.load_table())
        self.cb_order.bind("<<ComboboxSelected>>", lambda e: self.load_table())
        self.table.bind("<<TreeviewSelect>>", self.on_select)

        # ================= INIT =================
        self.load_table()

    # ==================================================
    # ================= BUSINESS LOGIC =================
    # ==================================================
    def load_table(self):
        keyword = self.entry_search.get()
        order = "ASC" if self.cb_order.get() == "Tăng dần" else "DESC"

        self.table.delete(*self.table.get_children())
        for c in get_courses(keyword, order):
            self.table.insert("", tk.END, values=c)

    def on_select(self, event):
        selected = self.table.selection()
        if not selected:
            return

        data = self.table.item(selected[0])["values"]
        self.selected_id = data[0]

        self.entry_code.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_credit.delete(0, tk.END)

        self.entry_code.insert(0, data[1])
        self.entry_name.insert(0, data[2])
        self.entry_credit.insert(0, data[3])

    def add(self):
        try:
            add_course(
                self.entry_code.get(),
                self.entry_name.get(),
                int(self.entry_credit.get())
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã thêm môn học")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def update(self):
        if not self.selected_id:
            messagebox.showwarning("Chọn", "Chọn môn cần cập nhật")
            return
        try:
            edit_course(
                self.selected_id,
                self.entry_code.get(),
                self.entry_name.get(),
                int(self.entry_credit.get())
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã cập nhật môn học")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
