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
    eligible = eligible_courses(course_list, taken)
    print("You are eligible to take the following courses: ")
    for course in eligible:
        print(course.course_number+ ": "+ course.course_name)

    concurrent = concurrent_courses(course_list, taken, eligible)
    print()
    print("You are eligible to take the following concurrent courses: ")
    for i in range(len(concurrent)):
        print(concurrent[i][0].course_number+":",concurrent[i][0].course_name)
        print("\t Required to take with: ",end="")
        for j in range(len(concurrent[i][1])-1):
            print(concurrent[i][1][j].course_number+":",concurrent[i][1][j].course_name,end=", ")
        print(concurrent[i][1][-1].course_number+":",concurrent[i][1][-1].course_name)
    print()


main()