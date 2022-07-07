#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "student.h"
#include "course.h"

void parseFiles(const std::string& course_file, const std::string& student_file,
                std::vector<Student>& students, std::vector<Course>& courses) {
    std::ifstream crs_str(course_file);
    char in = '\0';
    std::string course_name = "";
    // Keeps reading in characters until it is "done"
    while (crs_str >> in) {
        if (in == '\n') {
            // Add the full course to a vector of courses
            courses.push_back(Course(course_name));
            // Skip the next to characters to skip the course subject
            if (!(crs_str >> in) || !(crs_str >> in)) {
                break;
            }
        }
        else {
            course_name.push_back(in);
        }
    }

    std::ifstream std_str(student_file);
    // Skip first line of CSV file
    do {
        //Make sure it is a valid file
        if (!(std_str >> in)) break;
    } while (in != '\n');

    std::string str = "";
    std::string name = "";
    std::vector<std::string> std_courses;
    while (std_str >> in) {
        //Go to next Student
        if (in == '\n') {
            students.push_back(Student(name, std_courses));
        }
        //Go to next field
        else if (in == ',') {
            if (name == "") {
                name = str;
            }
            else {
                std_courses.push_back(str);
            }
        }
        //add characters to a string
        else {
            str.push_back(in);
        }
    }
}

int main(int argc, char* argv[]) {
    //Parse args
    if (argc != 3) {
        std::cerr << "Invalid command line arguments" <<
                  "Format should be:" << std::endl
                  << "./PROGRAM COURSE_LIST STUDENT_LIST"
                  << std::endl;
        exit(0);
    }
    std::string course_file;
    std::string student_file;
    course_file = argv[1];
    student_file = argv[2];

    //Parse files
    std::vector<Student> students;
    std::vector<Course> courses;
    parseFiles(course_file, student_file, students, courses);

    //Run scheduler

    //Output results
}