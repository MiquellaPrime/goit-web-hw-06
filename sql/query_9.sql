SELECT DISTINCT students.full_name AS student, subjects.name AS subject
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.id = 37
ORDER BY subjects.name;