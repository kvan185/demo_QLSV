import tkinter as tk
from tkinter import ttk, messagebox
from src.business.teacher_service import get_all_teachers, get_all_classes_status, set_advisor_for_class, get_teachers_for_combobox

class AdminAssignAdvisorForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padx=10, pady=10)

        self.class_map = {}
        self.teacher_map = {}

        # ================= TITLE =================
        tk.Label(
            self,
            text="QUẢN LÝ CỐ VẤN HỌC TẬP",
            font=("Arial", 15, "bold")
        ).pack(pady=5)

        # ================= FILTER =================
        filter_frame = tk.Frame(self)
        filter_frame.pack(fill=tk.X, pady=5)

        tk.Label(filter_frame, text="Trạng thái:").pack(side=tk.LEFT)
        self.cb_status = ttk.Combobox(
            filter_frame,
            state="readonly",
            width=15,
            values=["Tất cả", "Đã gán", "Chưa gán"]
        )
        self.cb_status.current(0)
        self.cb_status.pack(side=tk.LEFT, padx=5)

        ttk.Button(
            filter_frame,
            text="Làm mới",
            command=self.load_table
        ).pack(side=tk.LEFT, padx=10)

        # ================= TABLE =================
        table_frame = tk.Frame(self)
        table_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        columns = ("class", "major", "advisor", "status")
        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=12
        )

        self.table.heading("class", text="Lớp")
        self.table.heading("major", text="Ngành")
        self.table.heading("advisor", text="Cố vấn")
        self.table.heading("status", text="Trạng thái")

        self.table.column("class", width=120)
        self.table.column("major", width=150)
        self.table.column("advisor", width=200)
        self.table.column("status", width=100)

        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient=tk.VERTICAL,
            command=self.table.yview
        )
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.table.bind("<<TreeviewSelect>>", self.on_select)

        # ================= ASSIGN AREA =================
        assign_frame = tk.LabelFrame(
            self,
            text="GÁN / ĐỔI CỐ VẤN",
            padx=10,
            pady=10
        )
        assign_frame.pack(fill=tk.X, pady=10)

        tk.Label(assign_frame, text="Lớp:").grid(row=0, column=0, sticky="w")
        self.lbl_class = tk.Label(assign_frame, text="---", width=30)
        self.lbl_class.grid(row=0, column=1, sticky="w")

        tk.Label(assign_frame, text="Cố vấn hiện tại:").grid(row=1, column=0, sticky="w")
        self.lbl_current = tk.Label(assign_frame, text="---", width=30)
        self.lbl_current.grid(row=1, column=1, sticky="w")

        tk.Label(assign_frame, text="Cố vấn mới:").grid(row=2, column=0, sticky="w")
        self.cb_teacher = ttk.Combobox(assign_frame, state="readonly", width=28)
        self.cb_teacher.grid(row=2, column=1, pady=5)

        ttk.Button(
            assign_frame,
            text="GÁN / CẬP NHẬT",
            width=20,
            command=self.assign_advisor
        ).grid(row=3, column=1, pady=10, sticky="e")

        # ================= LOAD DATA =================
        self.load_table()
        self.load_teachers()

    # =================================================
    def load_table(self):
        self.table.delete(*self.table.get_children())
        self.class_map.clear()

        status_filter = self.cb_status.get()

        for cid, cname, major, advisor in get_all_classes_status():
            status = "Đã gán" if advisor else "Chưa gán"

            if status_filter == "Đã gán" and not advisor:
                continue
            if status_filter == "Chưa gán" and advisor:
                continue

            self.class_map[cname] = cid

            self.table.insert(
                "",
                tk.END,
                values=(
                    cname,
                    major,
                    advisor if advisor else "(Chưa có)",
                    status
                )
            )


    def load_teachers(self):
        self.teacher_map.clear()
        values = []

        for tid, name in get_teachers_for_combobox():
            self.teacher_map[name] = tid
            values.append(name)

        self.cb_teacher["values"] = values
        if values:
            self.cb_teacher.current(0)

    def on_select(self, event):
        selected = self.table.focus()
        if not selected:
            return

        values = self.table.item(selected, "values")
        self.lbl_class.config(text=values[0])
        self.lbl_current.config(text=values[2])

    def assign_advisor(self):
        class_name = self.lbl_class.cget("text")
        teacher_name = self.cb_teacher.get()

        if not class_name or class_name == "---":
            messagebox.showwarning("Lỗi", "Chưa chọn lớp")
            return

        if not teacher_name:
            messagebox.showwarning("Lỗi", "Chưa chọn giảng viên")
            return

        try:
            set_advisor_for_class(
                self.class_map[class_name],
                self.teacher_map[teacher_name]
            )

            messagebox.showinfo("OK", "Gán cố vấn thành công")
            self.load_table()

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))

