from pymongo import MongoClient

students = open('peeps.csv', 'r')
courses = open('courses.csv', 'r')

server = MongoClient('149.89.150.100')

db = server['pyschic-potato']

c = db['psychic-potato']['students']

students = students.read().split()

courses = courses.read().split()

courses.pop(0)

students.pop(0)

def db_build():
    for student in students:
        info = student.split(',')
        student_dict = {}
        student_dict['name'] = info[0]
        student_dict['age'] = int(info[1])
        student_dict['id'] = int(info[2])
        course_info = []
        for course in courses:
            data = course.split(',')
            if student_dict['id'] == int(data[2]):
                course_dict = {}
                course_dict['code'] = data[0]
                course_dict['mark'] = int(data[1])
                course_info.append(course_dict)
        student_dict['courses'] = course_info
        c.insert_one(student_dict)

def getAverages():
    db_info = c.find()
    l = []
    for student in db_info:
        info = []
        info.append(student['name'])
        info.append(student['id'])
        avg = 0
        count = 0
        for course in student['courses']:
            avg += course['mark']
            count += 1
        avg = avg / count
        info.append(avg)
        l.append(info)
    return l
                
def printAverages(avgList):
    for student in avgList:
        studentString = student[0] + ", "  + str(student[1]) + ", " + str(student[2])
        print(studentString)

c.remove()
db_build()
print(c.count())
printAverages(getAverages())


    

