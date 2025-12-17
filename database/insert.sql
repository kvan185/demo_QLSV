USE school_management;

-- ======================
-- USERS
-- ======================
INSERT INTO users (username, password, role) VALUES
('admin', 'admin123', 'admin'),
('teacher1', 'teacher123', 'teacher'),
('student1', 'student123', 'student');

-- ======================
-- CLASSES
-- ======================
INSERT INTO classes (class_name, major) VALUES
('CNTT1', 'Công nghệ thông tin'),
('CNTT2', 'Công nghệ thông tin'),
('KTPM1', 'Kỹ thuật phần mềm'),
('KTPM2', 'Kỹ thuật phần mềm');
-- ======================
-- STUDENTS
-- ======================
INSERT INTO students (student_code, full_name, birth_year, class_id) VALUES
('SV001', 'Nguyễn Văn An', 2002, 1),
('SV002', 'Trần Thị Bình', 2003, 1),
('SV003', 'Lê Văn Cường', 2002, 2),
('SV004', 'Phạm Thị Dung', 2001, 3);

-- ======================
-- COURSES
-- ======================
INSERT INTO courses (course_code, course_name, credit) VALUES
('CS101', 'Lập trình Python', 3),
('CS102', 'Cơ sở dữ liệu', 3),
('CS103', 'Cấu trúc dữ liệu', 4);

-- ======================
-- TEACHERS
-- ======================
INSERT INTO teachers (teacher_code, full_name, degree) VALUES
('GV01', 'Nguyễn Văn Hùng', 'ThS'),
('GV02', 'Trần Thị Mai', 'TS');

-- ======================
-- COURSE CLASSES
-- ======================
INSERT INTO course_classes (course_id, teacher_id, semester, school_year) VALUES
(1, 1, 'HK1', '2024-2025'),
(2, 1, 'HK1', '2024-2025'),
(3, 2, 'HK2', '2024-2025');

-- ======================
-- ENROLLMENTS
-- ======================
INSERT INTO enrollments (student_id, course_class_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(3, 3);

-- ======================
-- GRADES
-- ======================
INSERT INTO grades (student_id, course_id, score) VALUES
(1, 1, 8.5),
(1, 2, 7.0),
(2, 1, 9.0),
(3, 3, 6.5);

-- ======================
-- SEMESTERS
-- ======================
INSERT INTO semesters (name, start_date, end_date) VALUES
('HK1 2024-2025', '2024-09-01', '2025-01-15'),
('HK2 2024-2025', '2025-02-01', '2025-06-30');

-- ======================
-- GRADE RULES
-- ======================
INSERT INTO grade_rules (course_id, min_score, pass_score) VALUES
(1, 0, 5.0),
(2, 0, 5.0),
(3, 0, 5.0);
