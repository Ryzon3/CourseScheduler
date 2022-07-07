#ifndef _COURSE_H_
#define _COURSE_H_

#include <string>

class Course {
public:
    // Constructor
    Course(const std::string& name_) : name(name_) {};

    // Retrieves name
    const std::string& getName() { return name;}

private:
    //Name of the course
    std::string name;
};

#endif