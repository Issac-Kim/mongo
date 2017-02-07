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

dictstudents = []

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

def makeDict(students):
    for item in students:
        student = item.split(',')
        studentdict = {}
        studentdict['name'] = student[0]
        studentdict['age'] = int(student[1])
        studentdict['id'] = student[2]
        temp = []
        for data in courses:
            if data[-1] == student[2]:
                items = data.split(',')
                temp.append({'code' : item[0], 'mark' : item[1]})
        studentdict['classes'] = temp
        dictstudents.append(studentdict)
    
        
def inputToDB(dictstudents):
    for element in dictstudents:
        num = element['id']
        for items in courses:
            course = items.split(',')
            if course[2] != num:
                c.insert_one(element)
                break
            else:
                element['classes'][course[0]]= int(course[1])

def getAverages():
    db_info = c.find()
    l = []
    for student in db_info:
        info = {}
        info['name'] = student['name']
        info['id'] = student['id']
        avg = 0
        count = 0
        for course in student['classes']:
            avg += course['mark']
            count += 1
        avg = avg / count
        info['average'] = avg
        l.append(info)
    return l
                

print(c.count())
print(getAverages())


    

