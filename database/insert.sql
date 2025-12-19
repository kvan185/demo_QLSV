USE school_management;

-- ======================
-- USERS (NGƯỜI DÙNG)
-- ======================
INSERT INTO users (username, password, role) VALUES
('admin', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'admin'),
('manager1', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'manager'),
('GV01', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'teacher'),
('GV02', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'teacher'),
('GV03', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'teacher'),
('GV04', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'teacher'),
('GV05', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'teacher'),
('GV06', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'teacher'),
('GV07', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'teacher'),
('GV08', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'teacher'),
('GV09', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'teacher'),
('GV10', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'teacher'),
('SV001', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV002', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV003', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV004', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV005', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV006', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV007', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV008', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV009', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV010', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV011', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV012', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV013', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV014', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV015', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV016', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV017', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV018', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV019', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV020', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV021', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV022', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV023', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV024', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student'),
('SV025', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'student');

-- ======================
-- TEACHERS (GIÁO VIÊN)
-- ======================
INSERT INTO teachers (teacher_code, full_name, degree) VALUES
('GV01', 'Nguyễn Văn Hùng', 'ThS'),
('GV02', 'Lê Thị Hương', 'TS'),
('GV03', 'Phạm Văn Nam', 'ThS'),
('GV04', 'Trần Thị Lan', 'TS'),
('GV05', 'Hoàng Văn Minh', 'ThS'),
('GV06', 'Vũ Thị Thanh', 'TS'),
('GV07', 'Đặng Văn Quang', 'ThS'),
('GV08', 'Bùi Thị Phương', 'TS'),
('GV09', 'Lý Văn Sơn', 'ThS'),
('GV10', 'Hồ Thị Ngọc', 'TS'),
('GV11', 'Phan Văn Tuấn', 'ThS'),
('GV12', 'Trần Thị Mai', 'TS');

-- ======================
-- CLASSES (LỚP)
-- ======================
INSERT INTO classes (class_name, major, advisor_id) VALUES
('CNTT1', 'Công nghệ thông tin', 1),
('CNTT2', 'Công nghệ thông tin', 1),
('CNTTCLC', 'Công nghệ thông tin', 2),
('QTKD1', 'Quản trị kinh doanh', 3),
('QTKD2', 'Quản trị kinh doanh', 3),
('QTKDCLC', 'Quản trị kinh doanh', 4),
('NN1', 'Ngôn ngữ Anh', 5),
('NN2', 'Ngôn ngữ Anh', 5),
('NNCLC', 'Ngôn ngữ Anh', 6),
('Tài chính-Ngân hàng', 'Tài chính-Ngân hàng', 7),
('TCNB2', 'Tài chính-Ngân hàng', 7),
('TCNBCLC', 'Tài chính-Ngân hàng', 8),
('KT1', 'Kế toán', 9),
('KT2', 'Kế toán', 9),
('KTCLC', 'Kế toán', 10),
('GVMT1', 'Giáo viên mầm non', 11),
('GVMT2', 'Giáo viên mầm non', 11),
('GVMTCLC', 'Giáo viên mầm non', 12);

-- ======================
-- STUDENTS (SINH VIÊN)
-- ======================
INSERT INTO students (student_code, full_name, birth_year, class_id) VALUES
('SV001', 'Nguyễn Văn An', 2002, 1),
('SV002', 'Trần Thị Bình', 2003, 1),
('SV003', 'Lê Văn Cường', 2002, 2),
('SV004', 'Phạm Hoàng Thành', 2001, 3),
('SV005', 'Hoàng Văn Đông', 2003, 2),
('SV006', 'Vũ Thị Em', 2002, 1),
('SV007', 'Đặng Văn Phú', 2003, 3),
('SV008', 'Bùi Thị Hạnh', 2001, 2),
('SV009', 'Trịnh Văn Khoa', 2002, 1),
('SV010', 'Lý Thị Lan', 2003, 3),
('SV011', 'Ngô Văn Mạnh', 2002, 2),
('SV012', 'Phan Thị Nga', 2001, 1),
('SV013', 'Dương Văn Phúc', 2003, 3),
('SV014', 'Cao Thị Quỳnh', 2002, 2),
('SV015', 'Lâm Văn Sơn', 2001, 1),
('SV016', 'Trần Thị Thu', 2003, 3),
('SV017', 'Võ Văn Tùng', 2002, 2),
('SV018', 'Hồ Thị Uyên', 2001, 1),
('SV019', 'Nguyễn Văn Vinh', 2003, 3),
('SV020', 'Lê Thị Xinh', 2002, 2),
('SV021', 'Phạm Văn Yên', 2001, 1),
('SV022', 'Hoàng Thị Ánh', 2003, 3),
('SV023', 'Vũ Văn Bách', 2002, 2),
('SV024', 'Đặng Thị Chi', 2001, 1),
('SV025', 'Phạm Thị Dung', 2001, 3);

-- ======================
-- COURSES (MÔN HỌC)
-- ======================
INSERT INTO courses (course_code, course_name, credit) VALUES
('CS101', 'Lập trình Python', 3),
('CS102', 'Cơ sở dữ liệu', 3),
('CS103', 'Cấu trúc dữ liệu', 4);

-- ======================
-- SEMESTERS (HỌC KỲ)
-- ======================
INSERT INTO semesters (name, start_date, end_date) VALUES
('HK1 2024-2025', '2024-09-01', '2025-01-15'),
('HK2 2024-2025', '2025-02-01', '2025-06-30');

-- ======================
-- COURSE CLASSES (LỚP HỌC PHẦN)
-- ======================
INSERT INTO course_classes (course_id, teacher_id, semester, school_year) VALUES
(1, 1, 'HK1', '2024-2025'),
(2, 1, 'HK1', '2024-2025'),
(3, 2, 'HK2', '2024-2025');

-- =======================
-- CLASS SCHEDULES (LỊCH HỌC)
-- =======================
INSERT INTO class_schedules (course_class_id, day_of_week, start_period, periods, room, total_sessions)
VALUES
(1, 2, 1, 3, 'A101', 15),
(1, 4, 1, 3, 'A101', 15),
(2, 3, 4, 3, 'B202', 15),
(3, 5, 2, 4, 'C303', 15);

-- ======================
-- EXAM SCHEDULES (LỊCH THI)
-- ======================
INSERT INTO exam_schedules (course_class_id, exam_date, start_time, duration, room) VALUES
(1, '2024-12-15', '09:00:00', 90, 'A101'),
(2, '2024-12-16', '13:00:00', 90, 'B202'),
(3, '2025-01-10', '09:00:00', 120, 'C303');

-- ======================
-- ENROLLMENTS (ĐĂNG KÝ HỌC PHẦN)
-- ======================
INSERT INTO enrollments (student_id, course_class_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(3, 3);

-- ======================
-- TUITION SETTINGS (HỌC PHÍ)
-- ======================
INSERT INTO tuition_settings (system_name, price_per_credit, coefficient)
VALUES
('Chính quy', 450000, 1),
('CLC', 450000, 1.3);

-- ======================
-- GRADE RULES (QUY ĐỊNH ĐIỂM)
-- ======================
INSERT INTO grade_rules (course_id, min_score, pass_score) VALUES
(1, 0, 5.0),
(2, 0, 5.0),
(3, 0, 5.0);

-- ======================
-- GRADES (ĐIỂM HỌC PHẦN)
-- ======================
INSERT INTO grades (student_id, course_id, score) VALUES
(1, 1, 8.5),
(1, 2, 7.0),
(2, 1, 9.0),
(3, 3, 6.5);
