SELECT s.full_name, ROUND(AVG(grade), 2) AS avg_grade
FROM grades
LEFT JOIN students AS s ON grades.student_id = s.id
GROUP BY s.full_name
ORDER BY avg_grade DESC
LIMIT 5;