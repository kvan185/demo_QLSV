CREATE DATABASE IF NOT EXISTS school_management
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE school_management;

-- ======================
-- BẢNG NGƯỜI DÙNG
-- ======================
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255),
    role ENUM('admin','manager','teacher','student'),
    ref_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ======================
-- BẢNG MÔN HỌC
-- ======================
CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    credit INT NOT NULL
);

-- ======================
-- CÀI ĐẶT HỌC PHÍ
-- ======================
CREATE TABLE tuition_settings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    system_name VARCHAR(50),     -- Chính quy, Chất lượng cao...
    price_per_credit FLOAT,      -- Giá 1 tín chỉ
    coefficient FLOAT DEFAULT 1  -- Hệ số
);

-- ======================
-- GIÁO VIÊN
-- ======================
CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_code VARCHAR(20) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    degree VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ======================
-- BẢNG LỚP (BẮT BUỘC)
-- ======================
CREATE TABLE classes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(50) UNIQUE NOT NULL,
    major VARCHAR(100),
    advisor_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_class_advisor
        FOREIGN KEY (advisor_id)
        REFERENCES teachers(id)
        ON DELETE SET NULL
);

-- ======================
-- LỚP HỌC PHẦN
-- ======================
CREATE TABLE course_classes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    teacher_id INT NOT NULL,
    semester VARCHAR(20),
    school_year VARCHAR(20),

    FOREIGN KEY (course_id) REFERENCES courses(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

-- ======================
-- BẢNG SINH VIÊN
-- ======================
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_code VARCHAR(20) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    birth_year INT,
    class_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_student_class
        FOREIGN KEY (class_id)
        REFERENCES classes(id)
        ON DELETE SET NULL,
        credit INT NOT NULL DEFAULT 0
);

-- ======================
-- ĐĂNG KÝ HỌC PHẦN
-- ======================
CREATE TABLE enrollments (
    student_id INT,
    course_class_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id, course_class_id),

    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_class_id) REFERENCES course_classes(id)
);

-- ======================
-- LỊCH HỌC PHẦN
-- ======================
CREATE TABLE class_schedules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_class_id INT NOT NULL,
    day_of_week TINYINT NOT NULL, -- 2 = Thứ 2 ... 7 = Thứ 7
    start_period INT NOT NULL,    -- tiết bắt đầu
    periods INT NOT NULL,         -- số tiết / buổi
    room VARCHAR(50),
    total_sessions INT NOT NULL,  -- tổng số buổi (vd: 15)

    FOREIGN KEY (course_class_id)
        REFERENCES course_classes(id)
        ON DELETE CASCADE
);

-- ======================
-- LỊCH THI
-- ======================
CREATE TABLE exam_schedules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_class_id INT NOT NULL,
    exam_date DATE NOT NULL,
    start_time TIME NOT NULL,
    duration INT NOT NULL,     -- phút
    room VARCHAR(50),
    exam_type VARCHAR(20),     -- Giữa kỳ / Cuối kỳ

    FOREIGN KEY (course_class_id)
        REFERENCES course_classes(id)
        ON DELETE CASCADE
);

-- ======================
-- ĐIỂM
-- ======================
CREATE TABLE grades (
    student_id INT,
    course_id INT,
    score FLOAT CHECK (score BETWEEN 0 AND 10),
    PRIMARY KEY (student_id, course_id),

    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
);

-- ======================
-- HỌC KỲ
-- ======================
CREATE TABLE semesters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    start_date DATE,
    end_date DATE
);

-- ======================
-- QUY ĐỊNH ĐIỂM
-- ======================
CREATE TABLE grade_rules (
    course_id INT,
    min_score FLOAT,
    pass_score FLOAT,

    FOREIGN KEY (course_id) REFERENCES courses(id)
);
