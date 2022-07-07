#ifndef _STUDENT_H_
#define _STUDENT_H_

#include <string>
#include <vector>

class Student {
public:
    // Constructor
    Student(const std::string& name_, const std::vector<std::string>& courses_) :
        name(name_), courses(courses_) {};

    // Retrieves name
    const std::string& getName() { return name;}

    // Retrieves courses
    const std::vector<std::string>& getCourses() { return courses;}

private:
    //Name of the student
    std::string name;
    std::vector<std::string> courses;
};

#endif