# connect to a database and fetch the data from the database and display the data in the console

import sqlite3

def db_connection():
    conn = sqlite3.connect('student_marks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS student_marks (name text, marks integer)''')
    c.execute("INSERT INTO student_marks VALUES ('John', 70)")
    c.execute("INSERT INTO student_marks VALUES ('Kyle', 60)")
    c.execute("INSERT INTO student_marks VALUES ('Steve', 50)")
    c.execute("INSERT INTO student_marks VALUES ('Marsh', 40)")
    c.execute("INSERT INTO student_marks VALUES ('Lucie', 50)")
    c.execute("INSERT INTO student_marks VALUES ('Rama', 70)")
    c.execute("INSERT INTO student_marks VALUES ('Krishna', 30)")
    c.execute("INSERT INTO student_marks VALUES ('Mahesh', 40)")
    c.execute("INSERT INTO student_marks VALUES ('Suresh', 40)")
    c.execute("INSERT INTO student_marks VALUES ('Naresh', 60)")
    conn.commit()
    c.execute("SELECT * FROM student_marks")
    data = c.fetchall()
    print("Student data:", end=" ")
    for i in data:
        print(i[0], ":", i[1], end=", ")
    print("\n")
    print("third highest scored candidate names: ")

    third_max_query = """SELECT name, marks FROM (
                            SELECT name, marks, DENSE_RANK() OVER (ORDER BY marks DESC) AS r
                            FROM student_marks
                          ) AS subquery
                          WHERE r = 3;"""
    c.execute(third_max_query)
    data = c.fetchall()
    print(data)
    conn.close()

if __name__ == '__main__':
    db_connection()
    # Output:
    # Student data: John : 70, Kyle : 60, Steve : 50, Marsh : 40, Lucie : 50, Rama : 70, Krishna : 30, Mahesh : 40, Suresh : 40, Naresh : 60,
