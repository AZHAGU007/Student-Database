import sqlite3

def create_connection():
	connection=sqlite3.connect("Students.db")
	return connection

def create_table():
	connection=create_connection()
	cursor=connection.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS students(id TEXT,
	name STRING NOT NULL,
	age INTEGER(2),
	marks INTEGER(3))""")
	connection.commit()
	connection.close()


def add_student(id,name,age,marks):
	connection=create_connection()
	cursor=connection.cursor()
	cursor.execute("""INSERT INTO students(id,name,age,marks) VALUES (?,?,?,?)""",(id,name,age,marks))
	connection.commit()
	connection.close()
	print("Student added!")

def view_students():
	connection=create_connection()
	cursor=connection.cursor()
	cursor.execute("""SELECT *FROM students""")
	rows=cursor.fetchall()
	connection.close()
	for row in rows:
		print(row)
	
def update_marks(student_id,new_marks):
	connection=create_connection()
	cursor=connection.cursor()
	cursor.execute("""UPDATE students SET marks=? WHERE id=? """,(new_marks,student_id))
	connection.commit()
	connection.close()
	print("Marks Updated!")

def delete_student(student_id):
	connection=create_connection()
	cursor=connection.cursor()
	cursor.execute("""DELETE FROM students WHERE id=?""",(student_id,))
	connection.commit()
	connection.close()
	print("Student Deleted!")


create_table()

while True:
	print("\n=== Student Database System ===")
	print("1. Add Student")
	print("2. View All Students")
	print("3. Update Marks")
	print("4. Delete Student")
	print("5. Exit")

	choice=int(input("Enter Choice: "))
	if choice==1:
		id=input("ID: ")
		name=input("Name: ")
		age=int(input("Age: "))
		marks=int(input("Marks: "))
		add_student(id,name,age,marks)
	elif choice==2:
		view_students()
	elif choice==3:
		sid=input("Student ID: ")
		marks=float(input("New Marks: "))
		update_marks(sid,marks)
	elif choice==4:
		sid=input("Student ID: ")
		delete_student(sid)
	else :
		break
