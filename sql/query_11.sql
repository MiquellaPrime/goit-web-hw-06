SELECT students.full_name AS student,
       teachers.full_name AS teacher,
       subjects.name AS subject,
       ROUND(AVG(grades.grade), 2) AS avg_grade
FROM grades
JOIN students ON grades.student_id = students.id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.id = 26 AND teachers.id = 1
GROUP BY students.full_name, teachers.full_name, subjects.name
ORDER BY subjects.name;