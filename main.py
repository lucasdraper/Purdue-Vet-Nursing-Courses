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

    flag = True
    while flag:
        print("")
        change_q = input("Would you like to change any courses you have taken? (y/n): ")
        while change_q != 'y' and change_q != 'n':
            print("Invalid input")
            change_q = input("Enter 'y' or 'n': ")
        if change_q == 'y':
            print()
            change_dir = input("Would you like to add or delete a course? Enter 'add' or 'delete': ")
            while change_dir != 'add' and change_dir != 'delete':
                print("Invalid input")
                print()
                change_dir = input("Would you like to add or delete a course? Enter 'add' or 'delete': ")
            if change_dir == 'add':
                course = add_course(course_list, taken)
                if course != None:
                    taken.append(course)
            else:
                taken = delete_course(course_list, taken)
            print()
            for course in taken:
                print(course.course_number+ ": "+ course.course_name)
            print()
        else:
            flag = False

    print()

    print("Your finalized prior classes are: ")
    for course in taken:
        print(course.course_number+ ": "+ course.course_name)
    print()


    eligible = eligible_courses(course_list, taken)
    print("You are eligible to take the following courses: ")
    for course in eligible:
        print(course.course_number+ ": "+ course.course_name, "(Credits: "+str(course.credits)+")")

    concurrent = concurrent_courses(course_list, taken, eligible)
    print()
    print("You are eligible to take the following concurrent courses: ")
    for i in range(len(concurrent)):
        print(concurrent[i][0].course_number+":",concurrent[i][0].course_name, "(Credits: "+str(concurrent[i][0].credits)+")")
        print("\t Required to take with: ",end="")
        for j in range(len(concurrent[i][1])-1):
            print(concurrent[i][1][j].course_number+":",concurrent[i][1][j].course_name,end=", ")
        print(concurrent[i][1][-1].course_number+":",concurrent[i][1][-1].course_name)
    print()


main()