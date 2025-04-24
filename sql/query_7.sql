SELECT students.full_name AS student, groups.name AS group_name, subjects.name AS subject, grades.grade, grades.graded_at
FROM students
JOIN groups ON students.group_id = groups.id
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.group_id = 3 AND subjects.id = 4
ORDER BY students.full_name, grades.graded_at;