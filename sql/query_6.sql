SELECT students.full_name AS student, groups.name AS group_name
FROM students
JOIN groups ON students.group_id = groups.id
WHERE group_id = 1
ORDER BY students.full_name;