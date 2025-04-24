SELECT teachers.full_name AS teacher, subjects.name AS subject, ROUND(AVG(grades.grade), 2) AS avg_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.id = 1
GROUP BY grades.subject_id, subjects.name
ORDER BY subjects.name;