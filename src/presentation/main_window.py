import tkinter as tk
from tkinter import ttk, messagebox

# ===== IMPORT CÁC FORM =====
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
from src.presentation.class_schedule_form import ClassScheduleFrame
from src.presentation.exam_schedule_form import ExamScheduleFrame
from src.presentation.timetable_form import TimetableFrame
from src.presentation.admin_assign_advisor_form import AdminAssignAdvisorForm
from src.presentation.advisor_class_form import AdvisorClassFrame

class MainWindow(tk.Tk):
    def __init__(self, user):
        super().__init__()

        self.user = user   # {id, username, role, ref_id}
        self.current_frame = None

        self.title("Hệ thống quản lý trường học")
        self.geometry("1200x600")

        # ===== TOP BAR =====
        self.top = tk.Frame(self, bg="#f0f0f0", pady=5)
        self.top.pack(side=tk.TOP, fill=tk.X)

        # ===== CONTENT =====
        self.content = tk.Frame(self)
        self.content.pack(fill=tk.BOTH, expand=True)

        self.build_menu()
        self.show_home()

    # ================= MENU =================
    def build_menu(self):
        role = self.user["role"]

        # Xóa menu cũ (nếu có)
        for w in self.top.winfo_children():
            w.destroy()

        # ===== COMMON =====
        ttk.Button(self.top, text="Trang chủ", command=self.show_home)\
            .pack(side=tk.LEFT, padx=5)

        # ===== STUDENT =====
        if role == "student":
            ttk.Button(self.top, text="Thời khóa biểu", command=self.show_timetable)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Lịch thi", command=self.show_exam_schedule)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Học phí", command=self.show_tuition)\
                .pack(side=tk.LEFT, padx=5)

        # ===== TEACHER =====
        elif role == "teacher":
            ttk.Button(self.top, text="Lớp học phần", command=self.show_course_class)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Lịch dạy", command=self.show_class_schedule)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Nhập điểm", command=self.show_grade)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Lớp cố vấn", command=self.show_advisor)\
                .pack(side=tk.LEFT)

        # ===== MANAGER =====
        elif role == "manager":
            ttk.Button(self.top, text="Lớp", command=self.show_class)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Khóa học", command=self.show_course)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Giáo viên", command=self.show_teacher)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Lớp học phần", command=self.show_course_class)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Học kỳ", command=self.show_semester)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Gán cố vấn", command=self.show_assign_advisor)\
                .pack(side=tk.LEFT, padx=5)

        # ===== ADMIN =====
        elif role == "admin":
            ttk.Button(self.top, text="Sinh viên", command=self.show_student)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Giáo viên", command=self.show_teacher)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Lớp", command=self.show_class)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Khóa học", command=self.show_course)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Lớp học phần", command=self.show_course_class)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Đăng ký HP", command=self.show_enrollment)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Quy định điểm", command=self.show_grade_rule)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Học phí", command=self.show_tuition)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Lịch học", command=self.show_class_schedule)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Lịch thi", command=self.show_exam_schedule)\
                .pack(side=tk.LEFT, padx=5)
            ttk.Button(self.top, text="Gán cố vấn", command=self.show_assign_advisor)\
                .pack(side=tk.LEFT, padx=5)

        # ===== RIGHT SIDE =====
        ttk.Label(
            self.top,
            text=f"👤 {self.user['username']} ({role})",
            foreground="blue"
        ).pack(side=tk.RIGHT, padx=10)

        ttk.Button(self.top, text="Thoát", command=self.quit)\
            .pack(side=tk.RIGHT, padx=5)

    # ================= CORE =================
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
            font=("Arial", 18)
        ).pack(pady=30)

        tk.Label(
            frame,
            text=(
                f"Xin chào: {self.user['username']}\n"
                f"Vai trò: {self.user['role'].upper()}\n\n"
                "👉 Vui lòng chọn chức năng trên thanh menu"
            ),
            font=("Arial", 12),
            justify="center"
        ).pack()

        self.current_frame = frame

    # ================= SHOW FORM =================
    def show_student(self):
        self._show(StudentFrame)

    def show_class(self):
        self._show(ClassFrame)

    def show_course(self):
        self._show(CourseFrame)

    def show_grade(self):
        self._show(GradeFrame)

    def show_enrollment(self):
        self._show(EnrollmentFrame)

    def show_teacher(self):
        self._show(TeacherFrame)

    def show_course_class(self):
        self._show(CourseClassFrame)

    def show_semester(self):
        self._show(SemesterFrame)

    def show_grade_rule(self):
        self._show(GradeRuleFrame)

    def show_tuition(self):
        self._show(TuitionFrame)

    def show_class_schedule(self):
        self._show(ClassScheduleFrame)

    def show_exam_schedule(self):
        self._show(ExamScheduleFrame)

    def show_timetable(self):
        self._show(TimetableFrame)
        
    def show_advisor(self):
        self._show(AdvisorClassFrame)
        
    def show_assign_advisor(self):
        self._show(AdminAssignAdvisorForm)

    # ================= HELPER =================
    def _show(self, FrameClass):
        self.clear_content()
        self.current_frame = FrameClass(self.content)
        self.current_frame.pack(fill=tk.BOTH, expand=True)