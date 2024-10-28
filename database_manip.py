import sqlite3
db = sqlite3.connect('student_db.db')

cursor = db.cursor()

# Create table
db.commit()
cursor.execute('''
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
''')

db.commit()

# Insert redords into table
student_grades = [(55,'Carl Davis',61),(66,'Dennis Fredrickson',88),
                  (77,'Jane Richards',78),(12,'Peyton Sawyer',45),(2,'Lucas Brooke',99)]

cursor.executemany(''' INSERT INTO python_programming(id,name,grade) VALUES(?,?,?)''',
student_grades)

db.commit()


max_grade = 80
min_grade = 60

# Select all records with grades between 60 and 80
cursor.execute('''SELECT id, name,grade FROM python_programming WHERE grade >= ? AND grade <= ? ''',(min_grade, max_grade))
python_programming = cursor.fetchall()
print(python_programming)


# Change Carl Davis's grade to 65
grade = 65
id = 55
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id = ? ''',(grade, id))
db.commit()


# Delete Dennis Fredrickson's row
id = 66
cursor.execute('''DELETE FROM python_programming WHERE id = ? ''',(id,))
db.commit()


# Change grade to 80 for id numbers greater than 55
new_grade = 80
id = 55
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id > ? ''',(new_grade, id))
db.commit()


