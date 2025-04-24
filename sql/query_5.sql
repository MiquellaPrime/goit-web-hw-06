SELECT subjects.name AS subject, teachers.full_name AS teacher
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE subjects.teacher_id = 2
ORDER BY subjects.name;