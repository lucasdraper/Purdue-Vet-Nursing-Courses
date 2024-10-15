from course import Course

def Readin(file):
    courses = open(file, 'r')
    course_list = []
    for line in courses:
        line = line.strip()
        values = line.split('\t')
        
        course_name = values[1]
        course_number = values[0]
        pre_reqs_spot = values[2][1:-1]
        pre_reqs_spot = pre_reqs_spot.replace(' ', '')
        pre_reqs_spot = pre_reqs_spot.strip()

        credits = float(values[3])
        
        pre_reqs = pre_reqs_spot.split(',')
        course = Course(course_name, course_number, pre_reqs, credits)
        course_list.append(course)
    return course_list

def find_class(course_list, number):
    for course in course_list:
        if course.course_number == number:
            return course
    return None

def taken_courses(course_list):
    course_numbers = []
    num = int(input("How many courses have you taken so far? "))
    taken = []
    for i in range(num):
        course = input("Enter the course number: ")
        check = find_class(course_list, course)
        while check == None:
            print("Sorry, that course is not in our database.")
            course = input("Enter the course number: ")
            check = find_class(course_list, course)
        taken.append(check)
    print("You have taken the following courses: ")
    for course in taken:
        print(course.course_number, course.course_name)
    print()
    confirm = input("Do you need to add more? (y/n) ")
    while confirm == 'y':
        course = input("Enter the course number: ")
        check = find_class(course_list, course)
        while check == None:
            print("Sorry, that course is not in our database.")
            course = input("Enter the course number: ")
            check = find_class(course_list, course)
        taken.append(check)
        confirm = input("Do you need to add more? (y/n) ")
    return taken

def eligible_courses(course_list, taken):
    eligible = []
    potential = []
    for course in course_list:
        #print(course.course_name)
        prerequisites = course.pre_reqs
        elig_flag = True
        for prereq in prerequisites:
            if prereq == "":
                continue
            elif prereq[-1] != 'c':
                prereq_course = find_class(course_list, prereq)
                if prereq_course not in taken:
                    elig_flag = False
                    continue
            else:
                prereq_num = prereq[:-1]
                prereq_course = find_class(course_list, prereq_num)
                if prereq_course not in taken:
                    elig_flag = False
                    prereq_course = find_class(course_list, prereq_num)
                    potential.append([course, prereq_course])
        if elig_flag:
            eligible.append(course)
    for course in eligible:
        if course in taken:
            eligible.remove(course)
    for courses in potential:
        if courses[0] not in eligible and courses[1] not in eligible:
            potential.remove(course)


    print("You are eligible for the following courses in concurrency: ")
    for i in range(len(potential)):
        print(potential[i][0].course_name, "if you take", potential[i][1].course_name)

    return eligible, potential