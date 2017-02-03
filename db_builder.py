from pymongo import MongoClient

students = open('peeps.csv', 'r')
courses = open('courses.csv', 'r')

server = MongoClient('149.89.150.100')

db = server['pyschic-potato']

students = db.students

students = students.read().split()



