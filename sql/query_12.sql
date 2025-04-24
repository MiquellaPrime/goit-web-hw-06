SELECT students.full_name AS student,
       subjects.name AS subject,
       grades.grade,
       grades.graded_at
FROM grades
JOIN students ON grades.student_id = students.id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.group_id = 2
  AND grades.subject_id = 4
  AND grades.graded_at = (
      SELECT MAX(g.graded_at)
      FROM grades g
      WHERE g.student_id = grades.student_id AND g.subject_id = grades.subject_id
  )
ORDER BY students.full_name;