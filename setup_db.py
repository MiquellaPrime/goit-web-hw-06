import random
from sqlite3 import Connection

from faker import Faker

from database import create_connection

def create_all_tables(conn: Connection):
    c = conn.cursor()

    sql_create_groups_table = """
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );
    """
    c.execute(sql_create_groups_table)

    sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL,
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id)
    );
    """
    c.execute(sql_create_students_table)

    sql_create_teachers_table = """
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        full_name TEXT NOT NULL
    );
    """
    c.execute(sql_create_teachers_table)
    
    sql_create_subjects_table = """
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    );
    """
    c.execute(sql_create_subjects_table)

    sql_create_grades_table = """
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        graded_at DATE,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
    );
    """
    c.execute(sql_create_grades_table)
    
    conn.commit()


def populate_db(conn: Connection):
    c = conn.cursor()

    fake_data= Faker()
    
    # Додавання груп
    groups = ['Group A', 'Group B', 'Group C']
    c.executemany("INSERT INTO groups (name) VALUES (?)", [(g,) for g in groups])

    # Додавання викладачів
    teachers = [fake_data.name() for _ in range(random.randint(3, 5))]
    c.executemany("INSERT INTO teachers (full_name) VALUES (?)", [(t,) for t in teachers])

    # Отримання ID викладачів
    c.execute("SELECT id FROM teachers")
    teacher_ids = [row[0] for row in c.fetchall()]

    # Додавання предметів
    subjects = ['Math', 'Physics', 'History', 'Biology', 'Literature', 'Chemistry', 'Art', 'Philosophy']
    random_subjects = random.sample(subjects, random.randint(5, 8))
    subject_data = [(s, random.choice(teacher_ids)) for s in random_subjects]
    c.executemany("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", subject_data)

    # Отримання ID груп
    c.execute("SELECT id FROM groups")
    group_ids = [row[0] for row in c.fetchall()]

    # Додавання студентів
    students = [(fake_data.name(), random.choice(group_ids)) for _ in range(random.randint(30, 50))]
    c.executemany("INSERT INTO students (full_name, group_id) VALUES (?, ?) ", students)

    # Отримання ID студентів
    c.execute("SELECT id FROM students")
    student_ids = [row[0] for row in c.fetchall()]

    # Отримання ID предметів
    c.execute("SELECT id FROM subjects")
    subject_ids = [row[0] for row in c.fetchall()]

    # Додавання оцінок
    grades = []
    for student_id in student_ids:
        for _ in range(random.randint(15, 20)):
            subject_id = random.choice(subject_ids)
            grade = random.randint(60, 100)
            graded_at = fake_data.date_between(start_date='-1y', end_date='today')
            grades.append((student_id, subject_id, grade, graded_at))

    c.executemany(
        "INSERT INTO grades (student_id, subject_id, grade, graded_at) VALUES (?, ?, ?, ?)",
        grades
    )

    conn.commit()


if __name__ == '__main__':
    with create_connection() as conn:
        if conn is not None:
            create_all_tables(conn)
            print("Tables successfully created.")

            populate_db(conn)
            print("Database successfully seeded with random data.")
        else:
            print("Error! cannot create the database connection.")
