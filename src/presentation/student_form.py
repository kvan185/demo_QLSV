import tkinter as tk
from tkinter import ttk, messagebox
from src.business.student_service import (
    add_student,
    edit_student,
    search_students
)
from src.business.class_service import (
    get_classes,
    get_classes_for_combobox
)

class StudentFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.selected_id = None

        # ================= LEFT FORM =================
        form = tk.Frame(self, padx=10, pady=10)
        form.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(form, text="Mã SV").grid(row=0, column=0, sticky="w")
        self.entry_code = tk.Entry(form, width=25)
        self.entry_code.grid(row=0, column=1)

        tk.Label(form, text="Họ tên").grid(row=1, column=0, sticky="w")
        self.entry_name = tk.Entry(form, width=25)
        self.entry_name.grid(row=1, column=1)

        tk.Label(form, text="Năm sinh").grid(row=2, column=0, sticky="w")
        self.entry_year = tk.Entry(form, width=25)
        self.entry_year.grid(row=2, column=1)

        tk.Label(form, text="Lớp").grid(row=3, column=0, sticky="w")
        self.cb_form_class = ttk.Combobox(form, state="readonly", width=23)
        self.cb_form_class.grid(row=3, column=1)

        ttk.Button(form, text="Thêm", width=15, command=self.add).grid(row=4, column=0, pady=10)
        ttk.Button(form, text="Cập nhật", width=15, command=self.update).grid(row=4, column=1)

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

        tk.Label(filter_frame, text="Lớp").pack(side=tk.LEFT)
        self.cb_filter_class = ttk.Combobox(filter_frame, state="readonly", width=15)
        self.cb_filter_class.pack(side=tk.LEFT, padx=5)

        tk.Label(filter_frame, text="ID").pack(side=tk.LEFT)
        self.cb_order = ttk.Combobox(
            filter_frame,
            values=["Tăng dần", "Giảm dần"],
            state="readonly",
            width=12
        )
        self.cb_order.current(0)
        self.cb_order.pack(side=tk.LEFT)

        # ---------- TABLE ----------
        self.table = ttk.Treeview(
            right,
            columns=("id", "code", "name", "year", "class"),
            show="headings"
        )

        for col, text, w in [
            ("id", "ID", 60),
            ("code", "Mã SV", 100),
            ("name", "Họ tên", 180),
            ("year", "Năm sinh", 80),
            ("class", "Lớp", 80),
        ]:
            self.table.heading(col, text=text)
            self.table.column(col, width=w)

        self.table.pack(fill=tk.BOTH, expand=True)

        # ================= DATA MAP =================
        self.class_map = {"Tất cả": None}
        self.reverse_class_map = {}

        # ================= EVENTS =================
        self.entry_search.bind("<KeyRelease>", lambda e: self.load_table())
        self.cb_filter_class.bind("<<ComboboxSelected>>", lambda e: self.load_table())
        self.cb_order.bind("<<ComboboxSelected>>", lambda e: self.load_table())
        self.table.bind("<<TreeviewSelect>>", self.on_select)

        # ================= INIT =================
        self.load_classes()
        self.load_table()

    # ==================================================
    # ================= BUSINESS LOGIC =================
    # ==================================================
    def load_classes(self):
        self.class_map.clear()
        self.reverse_class_map.clear()

        filter_values = ["Tất cả"]
        form_values = []

        self.class_map["Tất cả"] = None

        for cid, cname in get_classes_for_combobox():
            filter_values.append(cname)
            form_values.append(cname)
            self.class_map[cname] = cid
            self.reverse_class_map[cid] = cname

        self.cb_filter_class["values"] = filter_values
        self.cb_form_class["values"] = form_values

        self.cb_filter_class.current(0)
        if form_values:
            self.cb_form_class.current(0)

    def load_table(self):
        keyword = self.entry_search.get()
        class_name = self.cb_filter_class.get()
        class_id = self.class_map.get(class_name)

        order = "ASC" if self.cb_order.get() == "Tăng dần" else "DESC"

        self.table.delete(*self.table.get_children())

        for s in search_students(keyword, class_id, order):
            self.table.insert("", tk.END, values=s)

    def on_select(self, event):
        selected = self.table.selection()
        if not selected:
            return

        data = self.table.item(selected[0])["values"]
        self.selected_id = data[0]

        self.entry_code.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_year.delete(0, tk.END)

        self.entry_code.insert(0, data[1])
        self.entry_name.insert(0, data[2])
        self.entry_year.insert(0, data[3])

        class_name = self.reverse_class_map.get(data[4])
        if class_name:
            self.cb_form_class.set(class_name)

    def add(self):
        try:
            class_id = self.class_map.get(self.cb_form_class.get())
            add_student(
                self.entry_code.get(),
                self.entry_name.get(),
                int(self.entry_year.get()),
                class_id
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã thêm sinh viên")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

    def update(self):
        if not self.selected_id:
            messagebox.showwarning("Chọn", "Chọn sinh viên cần cập nhật")
            return
        try:
            class_id = self.class_map.get(self.cb_form_class.get())
            edit_student(
                self.selected_id,
                self.entry_code.get(),
                self.entry_name.get(),
                int(self.entry_year.get()),
                class_id
            )
            self.load_table()
            messagebox.showinfo("OK", "Đã cập nhật sinh viên")
        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
