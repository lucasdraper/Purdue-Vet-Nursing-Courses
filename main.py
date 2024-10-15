class Course:
    def __init__(self, course_name, course_number, pre_reqs, credits):
        self.course_name = course_name
        self.course_number = course_number
        self.pre_reqs = pre_reqs
        self.credits = credits

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
        taken.append(course)
        confirm = input("Do you need to add more? (y/n) ")
    return taken

def eligible_courses(course_list, taken):
    eligible = []
    for course in course_list:
        print(course.course_name)
        prerequisites = course.pre_reqs
        for prereq in prerequisites:
            prereq = prereq.strip()
            if prereq == '':
                continue
            else:
                if prereq[-1] == 'c':
                    if prereq[:-1] not in taken:
                        break

                
    return eligible

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
        print(course.course_name)


main()