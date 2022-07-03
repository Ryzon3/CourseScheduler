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
# each student can take up to 8 courses with a minimum of 5
# for each empty slot a study hall is inserted
def generateStudents(amount, courses):
    names = open("us_names.txt", "r")
    lines = names.readlines()
    students = []

    for i in range(amount):
        student = {}
        student["name"] = choice(lines)[:-1]
        student["classes"] = []
        for i in range(8):
            subjs = []
            for clazz in student["classes"]:
                subjs.append(clazz[0])
            clazz = choice(courses)
            print(clazz[0])
            while clazz[0] in subjs and not(clazz[0] == 'Z'):
                clazz = choice(courses)
            student["classes"].append(clazz)
        students.append(students)
    return students

# main function
# generates the csv files
if __name__ == "__main__":
    courses = importCourses("course_list.txt")
    students = generateStudents(1000, courses)