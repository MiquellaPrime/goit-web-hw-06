SELECT subjects.name AS subject, groups.name AS group_, ROUND(AVG(grades.grade), 2) AS avg_grade
FROM grades
JOIN students ON grades.student_id = students.id
JOIN groups ON students.group_id = groups.id
JOIN subjects ON grades.subject_id = subjects.id
WHERE subject_id = 3
GROUP BY subjects.name, groups.name
ORDER BY avg_grade DESC;