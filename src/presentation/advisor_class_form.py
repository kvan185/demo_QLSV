import tkinter as tk
from tkinter import ttk
from src.business.teacher_service import get_advisor_class
from src.business.student_service import get_students_for_combobox_by_class


class AdvisorClassFrame(tk.Frame):
    def __init__(self, parent, teacher_id):
        super().__init__(parent)

        cls = get_advisor_class(teacher_id)

        if not cls:
            tk.Label(self, text="Bạn chưa được phân lớp cố vấn").pack()
            return

        class_id, class_name = cls

        tk.Label(
            self,
            text=f"Lớp cố vấn: {class_name}",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        table = ttk.Treeview(
            self,
            columns=("code", "name"),
            show="headings"
        )
        table.heading("code", text="MSSV")
        table.heading("name", text="Họ tên")
        table.pack(fill=tk.BOTH, expand=True)

        for sid, code, name in get_students_for_combobox_by_class(class_id):
            table.insert("", tk.END, values=(code, name))
