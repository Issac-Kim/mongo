from pymongo import MongoClient

teachers = open('teachers.csv', 'r')

server = MongoClient('149.89.150.100')

db = server['pyschic-potato']

c = db['psychic-potato']['teachers']

teachers = teachers.read().split()
teachers.pop(0)
c.remove()
def db_build():
    for teacher in teachers:
        students = db['psychic-potato']['students'].find()
        info = teacher.split(',')
        teacher_dict = {}
        teacher_dict['name'] = info[1]
        teacher_dict['code'] = info[0]
        teacher_dict['period'] = int(info[2])
        student_data = []
        for student in students:
            for course in student['courses']:
                if teacher_dict['code'] == course['code']:
                    student_data.append(student['id'])
        teacher_dict['students'] = student_data
        c.insert_one(teacher_dict)
        
teaches = c.find()
for teach in teaches:
    print(teach)