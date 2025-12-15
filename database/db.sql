CREATE DATABASE school_management
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE school_management;

-- Bảng người dùng
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255),
    role ENUM('admin','teacher','student')
);

-- Bảng lớp học
CREATE TABLE grades (
    student_id INT,
    course_class_id INT,
    score FLOAT CHECK (score BETWEEN 0 AND 10),

    PRIMARY KEY (student_id, course_class_id),

    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_class_id) REFERENCES course_classes(id)
);


-- Bảng sinh viên
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
        ON DELETE SET NULL
);

-- Bảng lớp học phần đăng ký
CREATE TABLE enrollments (
    student_id INT,
    course_class_id INT,
    PRIMARY KEY (student_id, course_class_id),

    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_class_id) REFERENCES course_classes(id)
);

-- Bảng môn học
CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    course_name VARCHAR(100) NOT NULL,
    credit INT NOT NULL
);

-- Bảng điểm
CREATE TABLE grades (
    student_id INT,
    course_id INT,
    score FLOAT CHECK (score BETWEEN 0 AND 10),
    PRIMARY KEY (student_id, course_id),

    CONSTRAINT fk_grade_student
        FOREIGN KEY (student_id)
        REFERENCES students(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_grade_course
        FOREIGN KEY (course_id)
        REFERENCES courses(id)
        ON DELETE CASCADE
);

-- Giáo viên
CREATE TABLE teachers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_code VARCHAR(20) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    degree VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bảng lớp học phần
CREATE TABLE course_classes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    teacher_id INT NOT NULL,
    semester VARCHAR(20),
    school_year VARCHAR(20),

    FOREIGN KEY (course_id) REFERENCES courses(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

-- Bảng học kỳ
CREATE TABLE semesters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    start_date DATE,
    end_date DATE
);


-- Bảng quy định điểm
CREATE TABLE grade_rules (
    course_id INT,
    min_score FLOAT,
    pass_score FLOAT,

    FOREIGN KEY (course_id) REFERENCES courses(id)
);
