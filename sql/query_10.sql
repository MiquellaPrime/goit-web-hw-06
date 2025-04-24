SELECT DISTINCT subjects.name AS subject, students.full_name AS student, teachers.full_name AS teacher
FROM grades
JOIN students ON grades.student_id = students.id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE student_id = 17 AND teachers.id = 3;