from course import Course
from functions import *


def main():
    course_list = Readin('Courses.txt')
    print("Welcome to the pre-requisite checker!")
    taken = taken_courses(course_list)
    print()
    print("You have taken the following courses: ")
    for course in taken:
        print(course.course_number+ ": "+ course.course_name)
    print()
    eligible, concurrent = eligible_courses(course_list, taken)
    print("You are eligible to take the following courses: ")
    for course in eligible:
        print(course.course_name)


main()