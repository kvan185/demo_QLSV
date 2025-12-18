import tkinter as tk
from tkinter import ttk

from src.presentation.student_form import StudentFrame
from src.presentation.class_form import ClassFrame
from src.presentation.course_form import CourseFrame
from src.presentation.grade_form import GradeFrame
from src.presentation.enrollment_form import EnrollmentFrame
from src.presentation.teacher_form import TeacherFrame
from src.presentation.course_class_form import CourseClassFrame
from src.presentation.semester_form import SemesterFrame
from src.presentation.grade_rule_form import GradeRuleFrame
from src.presentation.tuition_form import TuitionFrame

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
        ttk.Button(top, text="Khóa học", command=self.show_course).pack(side=tk.LEFT, padx=5)
        ttk.Button(top, text="Điểm", command=self.show_grade).pack(side=tk.LEFT, padx=5)
        ttk.Button(top, text="Đăng ký học phần", command=self.show_enrollment).pack(side=tk.LEFT, padx=5)
        ttk.Button(top, text="Giáo viên", command=self.show_teacher).pack(side=tk.LEFT, padx=5)
        ttk.Button(top, text="Lớp học phần", command=self.show_course_class).pack(side=tk.LEFT, padx=5)
        ttk.Button(top, text="Học kỳ", command=self.show_semester).pack(side=tk.LEFT, padx=5)
        ttk.Button(top, text="Quy định điểm", command=self.show_grade_rule).pack(side=tk.LEFT, padx=5)
        ttk.Button(top, text="Học phí", command=lambda: self.show_tuition()).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(top, text="Trang chủ", command=self.show_home).pack(side=tk.LEFT, padx=5)
        ttk.Button(top, text="Thoát", command=self.quit).pack(side=tk.RIGHT, padx=10)

        # ===== CONTENT AREA =====
        self.content = tk.Frame(self)
        self.content.pack(fill=tk.BOTH, expand=True)

        self.current_frame = None
        self.show_home()

    # ===== FRAME SWITCHER =====
    def clear_content(self):
        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None

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
                "• Quản lý điểm\n"
                "• Đăng ký học phần\n\n"
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

    def show_enrollment(self):
        self.clear_content()
        self.current_frame = EnrollmentFrame(self.content)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_teacher(self):
        self.clear_content()
        self.current_frame = TeacherFrame(self.content)
        self.current_frame.pack(fill=tk.BOTH, expand=True)

    def show_course_class(self):
        self.clear_content()
        self.current_frame = CourseClassFrame(self.content)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
    def show_semester(self):
        self.clear_content()
        self.current_frame = SemesterFrame(self.content)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
    def show_grade_rule(self):
        self.clear_content()
        self.current_frame = GradeRuleFrame(self.content)
        self.current_frame.pack(fill=tk.BOTH, expand=True)
        
    def show_tuition(self):
        self.clear_content()
        self.current_frame = TuitionFrame(self.content)
        self.current_frame.pack(fill=tk.BOTH, expand=True)    
    
# ===== ENTRY POINT =====
def main():
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
