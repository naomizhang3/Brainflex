DROP DATABASE IF EXISTS brainflex;
CREATE DATABASE IF NOT EXISTS brainflex;
USE brainflex;

SET FOREIGN_KEY_CHECKS = 0;

-- Creating core tables first
DROP TABLE IF EXISTS Students;
CREATE TABLE Students (
    user_id      INT PRIMARY KEY,
    nu_id        INT NOT NULL,
    first_name   VARCHAR(50) NOT NULL,
    MI           CHAR(1),
    last_name    VARCHAR(50),
    year         INT,
    major        VARCHAR(50),
    phone        VARCHAR(25) NOT NULL,
    pers_email   VARCHAR(50),
    nu_email     VARCHAR(50),
    accomm_descr VARCHAR(50),
    status       VARCHAR(25),
    active_min   INT
);

DROP TABLE IF EXISTS Tutors;
CREATE TABLE Tutors (
    user_id      INT PRIMARY KEY,
    nu_id        INT NOT NULL,
    first_name   VARCHAR(50) NOT NULL,
    MI           CHAR(1),
    last_name    VARCHAR(50),
    year         INT,
    major        VARCHAR(50),
    bio          TEXT,
    phone        VARCHAR(25) NOT NULL,
    pers_email   VARCHAR(50),
    nu_email     VARCHAR(50) NOT NULL,
    status       VARCHAR(25),
    calendar_url VARCHAR(50),
    active_min   INT
);

DROP TABLE IF EXISTS AcademicAdvisors;
CREATE TABLE AcademicAdvisors (
    advisors_id INT PRIMARY KEY,
    first_name  VARCHAR(50),
    MI          CHAR(1),
    last_name   VARCHAR(50),
    phone       VARCHAR(25) NOT NULL,
    pers_email  VARCHAR(50),
    nu_email    VARCHAR(50) NOT NULL,
    seniority   VARCHAR(25),
    status      VARCHAR(25),
    active_min  INT
);

DROP TABLE IF EXISTS Admins;
CREATE TABLE Admins (
    admin_id     INT PRIMARY KEY,
    first_name   VARCHAR(50),
    MI           CHAR(1),
    last_name    VARCHAR(50),
    phone        VARCHAR(25) NOT NULL,
    email        VARCHAR(75) NOT NULL,
    status       VARCHAR(50),
    active_min   INT,
    access_level DECIMAL(1, 0)
);

-- Creating tables that reference the core tables
DROP TABLE IF EXISTS Uploads;
CREATE TABLE Uploads (
    upload_id INT PRIMARY KEY,
    user_id   INT NOT NULL,
    file_name CHAR(50),
    type      VARCHAR(50),
    timestamp datetime,
    CONSTRAINT uploads_user_fk FOREIGN KEY (user_id) REFERENCES Students (user_id)
);

DROP TABLE IF EXISTS Feedback;
CREATE TABLE Feedback (
    feedback_id INT PRIMARY KEY,
    user_id int,
    reviewed_by INT NOT NULL,
    anonymity   BOOLEAN,
    text        TEXT,
    timestamp   DATETIME,
    status      VARCHAR(50),
    CONSTRAINT feedback_fk FOREIGN KEY (reviewed_by) REFERENCES AcademicAdvisors (advisors_id),
    CONSTRAINT student_feedback_fk FOREIGN KEY (user_id) REFERENCES Students (user_id)

);


DROP TABLE IF EXISTS FlagTypes;
CREATE TABLE FlagTypes (
    type_id INT PRIMARY KEY,
    name    VARCHAR(50)
);


DROP TABLE IF EXISTS Flags;
CREATE TABLE Flags (
    flag_id       INT PRIMARY KEY,
    type_id       INT,
    submitted_by  INT,
    creation_time DATETIME,
    comment       VARCHAR(50),
    CONSTRAINT flags_tutor_fk
        FOREIGN KEY (submitted_by)
        REFERENCES Tutors (user_id)
        ON DELETE CASCADE,
    CONSTRAINT flag_type_fk FOREIGN KEY (type_id) REFERENCES FlagTypes (type_id)
);

DROP TABLE IF EXISTS Courses;
CREATE TABLE Courses (
    course_id  varchar(25),
    course_num INT,
    section    VARCHAR(50),
    professor  VARCHAR(50),
    PRIMARY KEY(course_id, course_num)
);

DROP TABLE IF EXISTS RegisteredCourses;
CREATE TABLE RegisteredCourses (
    user_id    INT,
    course_id  varchar(25),
    course_num int,
    PRIMARY KEY (user_id, course_id, course_num),
    CONSTRAINT registered_tutors_fk
        FOREIGN KEY (user_id)
        REFERENCES Tutors (user_id)
        ON DELETE CASCADE,
    CONSTRAINT registered_courses_fk FOREIGN KEY (course_id, course_num) REFERENCES Courses (course_id, course_num)
);

DROP TABLE IF EXISTS RequestTypes;
CREATE TABLE RequestTypes (
    type_id INT PRIMARY KEY,
    name    VARCHAR(50)
);

DROP TABLE IF EXISTS Requests;
CREATE TABLE Requests (
    request_id     INT PRIMARY KEY,
    type_id        INT,
    description    TEXT,
    status        VARCHAR(50),
    sent_by       INT,
    reviewed_by   INT,
    CONSTRAINT request_type_fk FOREIGN KEY (type_id) REFERENCES RequestTypes (type_id),
    CONSTRAINT request_admin_fk FOREIGN KEY (reviewed_by) REFERENCES Admins (admin_id),
    CONSTRAINT request_advisor_fk FOREIGN KEY (sent_by) REFERENCES AcademicAdvisors (advisors_id)
);

DROP TABLE IF EXISTS Bookings;
CREATE TABLE Bookings (
    booking_id     INT PRIMARY KEY,
    status         BOOLEAN,
    creation_time  DATETIME,
    scheduled_time  DATETIME
);

DROP TABLE IF EXISTS BookingParticipants;
CREATE TABLE BookingParticipants (
    tutor_id    INT,
    student_id  INT,
    booking_id  INT,
    rating      TINYINT,
    PRIMARY KEY (tutor_id, student_id, booking_id),
    CONSTRAINT booking_tutor_fk FOREIGN KEY (tutor_id) REFERENCES Tutors (user_id),
    CONSTRAINT booking_student_fk FOREIGN KEY (student_id) REFERENCES Students (user_id),
    CONSTRAINT booking_fk
        FOREIGN KEY (booking_id)
        REFERENCES Bookings (booking_id)
        ON DELETE CASCADE

);

DROP TABLE IF EXISTS PaymentMethods;
CREATE TABLE PaymentMethods (
    method_id INT PRIMARY KEY,
    name      VARCHAR(50)
);

DROP TABLE IF EXISTS Transactions;
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    recipient_id   INT,
    reviewed_by    INT,
    booking_id     INT,
    method_id      INT,
    status         VARCHAR(25),
    payment_date   DATETIME,
    amount         DECIMAL(10, 2),
    earned_date    DATETIME,
    CONSTRAINT transaction_tutor_fk FOREIGN KEY (recipient_id) REFERENCES Tutors (user_id),
    CONSTRAINT transaction_method_fk FOREIGN KEY (method_id) REFERENCES PaymentMethods (method_id),
    CONSTRAINT transaction_booking_fk
        FOREIGN KEY (booking_id)
        REFERENCES Bookings (booking_id)
        ON DELETE CASCADE,
    CONSTRAINT reviewer_fk FOREIGN KEY (reviewed_by) REFERENCES AcademicAdvisors(advisors_id)

);

DROP TABLE IF EXISTS Backups;
CREATE TABLE Backups (
    backup_id VARCHAR(50) PRIMARY KEY,
    status    BOOLEAN,
    timestamp DATETIME,
    admin_id  INT NOT NULL,
    CONSTRAINT backup_admin_fk FOREIGN KEY (admin_id) REFERENCES Admins (admin_id)
);

DROP TABLE IF EXISTS LogTypes;
CREATE TABLE LogTypes (
    type_id INT PRIMARY KEY,
    name    VARCHAR(50),
    details TEXT
);

DROP TABLE IF EXISTS SystemLogs;
CREATE TABLE SystemLogs (
    log_id         INT PRIMARY KEY,
    type_id        INT,
    status         BOOLEAN,
    creation_date  DATETIME,
    resolved_date  DATETIME,
    reviewed_by    INT,
    CONSTRAINT log_type_fk FOREIGN KEY (type_id) REFERENCES LogTypes (type_id),
    CONSTRAINT log_admin_fk FOREIGN KEY (reviewed_by) REFERENCES Admins (admin_id)
);

SET FOREIGN_KEY_CHECKS = 1;
