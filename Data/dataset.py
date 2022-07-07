import csv
from random import choice

# reads in courses from text file
def importCourses(courseList):
    CL = open(courseList, 'r')
    lines = CL.readlines()
    output = []
    for line in lines:
        i = line.index(' ')
        temp = [line[:i], line[i+1:-1]]
        output.append(temp)
    return output

# generates a random dataset of students
# each student can take up to 8 courses
# study halls are more heavily weighted 
def generateStudents(amount, courses):
    names = open("us_names.txt", "r")
    lines = names.readlines()
    students = {}

    for i in range(amount):
        student = {}
        student["name"] = choice(lines)[:-1]
        student["classes"] = []
        for i in range(8):
            subjs = []
            for clazz in student["classes"]:
                subjs.append(clazz[0])
            clazz = choice(courses)
            while clazz[0] in subjs and not(clazz[0] == 'Z'):
                clazz = choice(courses)
            student["classes"].append(clazz)
        classes = student["classes"]
        fixedClasses = []
        for clazz in classes:
            fixedClasses.append(clazz[1])
        student["classes"] = fixedClasses
        students[student["name"]] = student
    return students

# main function
# generates the csv files
if __name__ == "__main__":
    courses = importCourses("course_list.txt")
    students = generateStudents(10, courses)

    f = open('students.csv', 'w')
    # write header to CSV
    f.write("Name,Class 1,Class 2,Class 3,Class 4,Class 5,Class 6,Class 7,Class 8\n")
    for student in students:
        txt = students[student]["name"]
        for clazz in students[student]["classes"]:
            txt = txt + ","
            txt = txt + clazz
        txt = txt + "\n"
        f.write(txt)
    f.close()