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

def makeDict(students):
    for item in students:
        student = item.split(',')
        studentdict = {}
        studentdict['name'] = student[0]
        studentdict['age'] = int(student[1])
        studentdict['id'] = student[2]
        studentdict['classes'] = {}
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
                
peep = c.find()
for p in peep:
    print(p)
    

