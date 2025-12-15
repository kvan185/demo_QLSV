import tkinter as tk
from tkinter import ttk
from src.presentation.student_form import StudentFrame
from src.presentation.class_form import ClassFrame
from src.presentation.course_form import CourseFrame
from src.presentation.grade_form import GradeFrame

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hệ thống quản lý trường học")
        self.geometry("1000x520")

        # ===== TOP BAR =====
        top = tk.Frame(self, bg="#f0f0f0", pady=5)
        top.pack(side=tk.TOP, fill=tk.X)

        ttk.Button(top, text="Sinh viên", command=self.show_student).pack(side=tk.LEFT, padx=5)
        ttk.Button(top, text="Lớp", command=self.show_class).pack(side=tk.LEFT, padx=5)
        ttk.Button(top, text="Thoát", command=self.quit).pack(side=tk.RIGHT, padx=10)
        ttk.Button(top, text="Khóa học", command=self.show_course).pack(side=tk.LEFT)
        ttk.Button(top, text="Điểm", command=self.show_grade).pack(side=tk.LEFT, padx=5)
        # ===== CONTENT AREA =====
        self.content = tk.Frame(self)
        self.content.pack(fill=tk.BOTH, expand=True)

        self.current_frame = None
        self.show_home()

    # ===== FRAME SWITCHER =====
    def clear_content(self):
        if self.current_frame:
            self.current_frame.destroy()

    def show_home(self):
        self.clear_content()
        frame = tk.Frame(self.content)
        frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            frame,
            text="👋 Chào mừng đến với Hệ thống Quản lý Trường học",
            font=("Arial", 16)
        ).pack(pady=30)

        tk.Label(
            frame,
            text=(
                "• Quản lý sinh viên\n"
                "• Quản lý lớp học\n"
                "• Quản lý khóa học\n"
                "• Quản lý điểm\n\n"
                "👉 Chọn chức năng ở thanh trên"
            ),
            font=("Arial", 11),
            justify="left"
        ).pack()

        self.current_frame = frame

    def show_student(self):
        self.clear_content()
        self.current_frame = StudentFrame(self.content)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_class(self):
        self.clear_content()
        self.current_frame = ClassFrame(self.content)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_course(self):
        self.clear_content()
        self.current_frame = CourseFrame(self.content)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_grade(self):
        self.clear_content()
        self.current_frame = GradeFrame(self.content)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
