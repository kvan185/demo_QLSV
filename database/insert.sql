USE school_management;

-- ============================
-- Dữ liệu lớp học
-- ============================
INSERT INTO classes (class_name, major) VALUES
('DHTH01', 'Hệ thống thông tin'),
('DHTH02', 'Công nghệ thông tin'),
('DHTH03', 'Khoa học máy tính');

-- ============================
-- Dữ liệu sinh viên
-- ============================
INSERT INTO students (student_code, full_name, birth_year, class_id) VALUES
('SV001', 'Nguyễn Văn A', 2003, 1),
('SV002', 'Trần Thị B', 2004, 1),
('SV003', 'Lê Văn C', 2003, 2);

-- ============================
-- Dữ liệu môn học
-- ============================
INSERT INTO courses (course_code, course_name, credit) VALUES
('CSDL', 'Cơ sở dữ liệu', 3),
('OOAD', 'Phân tích thiết kế hướng đối tượng', 3),
('HTTT', 'Hệ thống thông tin', 3);

-- ============================
-- Dữ liệu điểm
-- ============================
INSERT INTO grades (student_id, course_id, score) VALUES
(1, 1, 8.5),
(1, 2, 7.8),
(2, 1, 9.0),
(3, 3, 8.2);
