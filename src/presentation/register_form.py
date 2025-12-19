import tkinter as tk
from tkinter import ttk, messagebox
from src.business.auth_service import register
from src.business.student_service import fetch_all_students
from src.business.teacher_service import fetch_all_teachers

class RegisterForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Đăng ký tài khoản")
        self.geometry("350x300")

        self.ref_map = {}

        tk.Label(self, text="Username").pack()
        self.entry_user = tk.Entry(self)
        self.entry_user.pack()

        tk.Label(self, text="Password").pack()
        self.entry_pass = tk.Entry(self, show="*")
        self.entry_pass.pack()

        tk.Label(self, text="Vai trò").pack()
        self.cb_role = ttk.Combobox(
            self,
            values=["student", "teacher", "admin", "manager"],
            state="readonly"
        )
        self.cb_role.pack()
        self.cb_role.current(0)

        tk.Label(self, text="Liên kết (SV / GV)").pack()
        self.cb_ref = ttk.Combobox(self, state="readonly")
        self.cb_ref.pack()

        ttk.Button(self, text="Đăng ký", command=self.do_register).pack(pady=10)

        self.cb_role.bind("<<ComboboxSelected>>", self.load_ref)
        self.load_ref()

    # =============================
    def load_ref(self, event=None):
        role = self.cb_role.get()
        self.ref_map.clear()

        if role == "student":
            values = []
            for sid, code, name, *_ in fetch_all_students():
                label = f"{code} - {name}"
                self.ref_map[label] = sid
                values.append(label)
            self.cb_ref["values"] = values
            if values:
                self.cb_ref.current(0)

        elif role == "teacher":
            values = []
            for tid, code, name, *_ in fetch_all_teachers():
                label = f"{code} - {name}"
                self.ref_map[label] = tid
                values.append(label)
            self.cb_ref["values"] = values
            if values:
                self.cb_ref.current(0)

        else:
            self.cb_ref["values"] = []
            self.cb_ref.set("")

    def do_register(self):
        try:
            role = self.cb_role.get()
            ref_id = None

            if role in ("student", "teacher"):
                ref_id = self.ref_map.get(self.cb_ref.get())

            register(
                self.entry_user.get(),
                self.entry_pass.get(),
                role,
                ref_id
            )

            messagebox.showinfo("OK", "Tạo tài khoản thành công")
            self.destroy()

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
