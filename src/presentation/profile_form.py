import tkinter as tk
from tkinter import ttk

from src.business.student_service import get_student_by_id
from src.business.teacher_service import get_teacher_by_id


class ProfileFrame(tk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent, padx=20, pady=20)

        self.user = user
        role = user["role"]

        tk.Label(
            self,
            text="👤 THÔNG TIN CÁ NHÂN",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        box = ttk.LabelFrame(self, text="Chi tiết")
        box.pack(fill=tk.X, padx=20, pady=20)

        if role == "student":
            self.show_student(box)
        elif role == "teacher":
            self.show_teacher(box)
        else:
            self.show_account(box)

    # ================= STUDENT =================
    def show_student(self, parent):
        s = get_student_by_id(self.user["ref_id"])

        if not s:
            tk.Label(
                parent,
                text="❌ Không tìm thấy thông tin sinh viên",
                foreground="red"
            ).pack(pady=10)
            return
    
        self.row(parent, "MSSV", s[1])
        self.row(parent, "Họ tên", s[2])
        self.row(parent, "Giới tính", s[3])
        self.row(parent, "Ngày sinh", s[4])
        self.row(parent, "Email", s[5])
        self.row(parent, "SĐT", s[6])
        self.row(parent, "Lớp", s[7])

    # ================= TEACHER =================
    def show_teacher(self, parent):
        t = get_teacher_by_id(self.user["ref_id"])
        # id, code, full_name, email, phone

        self.row(parent, "Mã GV", t[1])
        self.row(parent, "Họ tên", t[2])
        self.row(parent, "Email", t[3])
        self.row(parent, "SĐT", t[4])

    # ================= ADMIN / MANAGER =================
    def show_account(self, parent):
        self.row(parent, "Tài khoản", self.user["username"])
        self.row(parent, "Vai trò", self.user["role"].upper())

    # ================= HELPER =================
    def row(self, parent, label, value):
        f = tk.Frame(parent)
        f.pack(fill=tk.X, pady=4)

        tk.Label(f, text=label + ":", width=15, anchor="w").pack(side=tk.LEFT)
        tk.Label(f, text=value, anchor="w", font=("Arial", 11, "bold"))\
            .pack(side=tk.LEFT)
