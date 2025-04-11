USE brainflex;



INSERT INTO Students (user_id, nu_id, first_name, MI, last_name, year, major, phone, pers_email, nu_email, accomm_descr,
                      `status`, active_min)
VALUES (0, 002377665, 'Alex', 'E', 'Gilliland', 1, 'Business Administration', '8089243167', 'agilliland@gmail.com',
        'gilliland.a@northeastern.edu', NULL, 'Valid', 100),
       (1, 002389786, 'Rai', 'S', 'Makaraju', 1, 'Computer Science', '2283905467', 'rainism@gmail.com',
        'makaraju.r@gmail.com', NULL, 'Valid', 900);

INSERT INTO Tutors (user_id, first_name, MI, last_name, nu_id, calendar_url, year, major, bio, phone, pers_email,
                    nu_email, `status`, active_min)
VALUES (2, 'Sasha', NULL, 'Tchaikovsky', 002312345, 'https://calendar.google.com/calendar/', 3,
        'Computer Science and Business Administration', 'Hi, my name is Sasha! I use an interactive teaching style.',
        '1234567890', 'stchaik@gmail.com', 's.tchai@northeastern.edu', 'Valid', 700),
       (3, 'Yueran', NULL, 'Jia', '002367529', 'https://calendar.google.com/calendar/', 2,
        'Data Science', 'Hi, my name is Yuri! I use an incentive-based teaching style.',
        '4176503421', 'yuerjia@gmail.com', 'jia.yuer@northeastern.edu', 'Flagged', 120);

INSERT INTO Admins (admin_id, first_name, MI, last_name, phone, email, `status`, active_min, access_level)
VALUES (4, 'Allie', NULL, 'Smith', '123-456-7123', 'allie.s@gmail.com', 'valid', 100, 1),
 (5, 'Bob', 'L', 'Jones', '934-123-5474', 'bob.jones@yahoo.com', 'temporarily banned', 10, 2);

INSERT INTO AcademicAdvisors (advisors_id, first_name, MI, last_name, phone, pers_email, nu_email, seniority, `status`, active_min)
VALUES (6, 'Alexander', 'P', 'Xander', '923-642-1094', 'xander.a@gmail.com', 'xander.alex@northeastern.edu', 'senior', 'valid',
 100000),
(7, 'Olivia', NULL, 'Jade', '123-121-9842', NULL, 'jade.olivia@northeastern.edu', 'associate', 'valid', 90);

INSERT INTO Uploads (upload_id, user_id, file_name, type, timestamp)
VALUES (0, 0, 'ch7', '.pdf', '2025-02-28 05:25:01'),
       (1, 1, 'hw1', '.py', '2025-03-15 10:07:32');

INSERT INTO Feedback (feedback_id, user_id, reviewed_by, anonymity, text, timestamp, `status`)
VALUES (0, NULL, 6, 1, 'Slow loading time', '2024-10-21 12:31:45', 'Addressed'),
       (1, 0, 7, 0, 'Buggy interface', '2025-01-31 07:18:21', 'Pending');

INSERT INTO FlagTypes (type_id, name)
VALUES (0, 'Inappropriate language'),
       (1, 'Frequent no-shows');

INSERT INTO Flags (flag_id, type_id, submitted_by, creation_time, comment)
VALUES (0, 0, 2, '2025-06-19 03:19:33', 'Language in bio'),
       (1, 1, 3, '2025-06-20 04:19:21', 'Sasha missed 2 meetings');

INSERT INTO Courses (course_id, course_num, section, professor)
VALUES ('CS', 3200, '08', 'Fontenot'),
       ('DS', 2500, '05', 'Strange');

INSERT INTO RegisteredCourses (user_id, course_id, course_num)
VALUES (2, 'CS', 3200),
       (3, 'DS', 2500);

INSERT INTO Bookings (booking_id, `status`, creation_time, scheduled_time)
VALUES (0, 1, '2023-08-19 13:21:41', '2023-08-20 8:00:00'),
       (1, 1, '2024-05-09 12:00:38', '2024-05-09 12:30:00');

INSERT INTO BookingParticipants (tutor_id, student_id, booking_id, rating)
VALUES (2, 0, 0, 5),
       (3, 1, 1, NULL);

INSERT INTO LogTypes
VALUES (0, '404 Page Not Found', 'Tutor earnings page was not found'),
       (1, 'Database connection error', 'Failed to connect to database');

INSERT INTO SystemLogs
VALUES (0, 1, 1, '2025-03-25 12:00:09', CURRENT_TIMESTAMP, 4),
       (1, 0, 0, '2025-04-12 16:19:18', NULL, NULL);

INSERT INTO Backups
VALUES (0, 1, CURRENT_TIMESTAMP, 4),
       (1, 0, '2025-03-25 12:00:09', 5);

INSERT INTO RequestTypes
VALUES (0, 'Access to delete'),
       (1, 'Ability to ban user');

INSERT INTO Requests
VALUES (0, 0, 'Give me access plz', 'fufilled', 6, 5),
       (1, 1, 'Can I ban this user', 'pending', 7, 4);

INSERT INTO PaymentMethods
VALUES (0, 'credit card'),
(1, 'paypal');


INSERT INTO Transactions
VALUES (0, 2, 6, 0, 0, 'valid', '2025-03-28 16:08:48', 10.5, '2025-03-20 18:48:20'),
(1, 3, 7, 1, 0, 'valid', '2025-02-24 14:09:38', 10.5, '2025-02-19 15:39:03');

