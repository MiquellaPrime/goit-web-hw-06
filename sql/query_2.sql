SELECT sbj.name AS subject, std.full_name AS student, ROUND(AVG(g.grade), 2) AS avg_grade
FROM grades g
JOIN subjects sbj ON g.subject_id = sbj.id
JOIN students std ON g.student_id = std.id
WHERE g.subject_id = 5
GROUP BY g.subject_id, g.student_id
ORDER BY avg_grade DESC
LIMIT 1;
