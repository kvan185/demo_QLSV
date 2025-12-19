import tkinter as tk
from tkinter import messagebox
from src.business.auth_service import login


class LoginForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Đăng nhập")
        self.geometry("300x220")
        self.resizable(False, False)

        self.main_frame = None

        tk.Label(self, text="ĐĂNG NHẬP", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self, text="Username").pack()
        self.entry_user = tk.Entry(self)
        self.entry_user.pack()

        tk.Label(self, text="Password").pack()
        self.entry_pass = tk.Entry(self, show="*")
        self.entry_pass.pack()

        tk.Button(self, text="Đăng nhập", command=self.do_login).pack(pady=15)

    def do_login(self):
        try:
            user = login(
                self.entry_user.get(),
                self.entry_pass.get()
            )

            if not user:
                raise Exception("Sai tài khoản hoặc mật khẩu")

            # ❌ KHÔNG withdraw
            # self.withdraw()

            # Xóa toàn bộ widget login
            for w in self.winfo_children():
                w.destroy()

            from src.presentation.main_window import MainWindow

            self.main_frame = MainWindow(
                parent=self,
                user=user,
                on_logout=self.show_login
            )
            self.main_frame.pack(fill=tk.BOTH, expand=True)

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
        
    def show_login(self):
        if self.main_frame:
            self.main_frame.destroy()
        self.main_frame = None

        # Load lại giao diện login
        for w in self.winfo_children():
            w.destroy()

        self.__init__()
