import tkinter as tk
from tkinter import messagebox
from src.business.auth_service import login
from src.presentation.main_window import MainWindow

class LoginForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Đăng nhập")
        self.geometry("300x200")

        tk.Label(self, text="Username").pack()
        self.entry_user = tk.Entry(self)
        self.entry_user.pack()

        tk.Label(self, text="Password").pack()
        self.entry_pass = tk.Entry(self, show="*")
        self.entry_pass.pack()

        tk.Button(self, text="Đăng nhập", command=self.do_login).pack(pady=10)

    def do_login(self):
        try:
            user = login(
                self.entry_user.get(),
                self.entry_pass.get()
            )
            self.destroy()
            MainWindow(user).mainloop()

        except Exception as e:
            messagebox.showerror("Lỗi", str(e))
