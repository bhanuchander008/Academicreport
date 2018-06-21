import csv
import MySQLdb
HOST = 'localhost'
USER = 'root'
PASSWORD = 'bhanu123'
DATABASE = 'academic'
db = MySQLdb.connect(host = HOST,user = USER,passwd = PASSWORD,db = DATABASE)
cursor = db.cursor()

with open('/home/bhanu/dev/Academicreport/studentdetails/subject_faculty.csv','r') as subject_csv:
    subject_data = csv.reader(subject_csv)
    for y in subject_data:
        print (y)
        cursor.execute('INSERT INTO studentdetails_subjectfaculty (subject,name)values(%s ,%s )',(y[0],y[1]))

with open('/home/bhanu/dev/Academicreport/studentdetails/student_marks.csv','r') as marks_csv:
    student_data = csv.reader(marks_csv)
    for x in student_data:
        cursor.execute('INSERT INTO studentdetails_studentmarks(studentname,subject,marks) values(%s,%s,%s)',(x[0],x[1],x[2]))
db.commit()
cursor.close()
