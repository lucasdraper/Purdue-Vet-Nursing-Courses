from course import Course


def Readin(file):
    """Function to read in the courses from a file and create a list of Course objects.
    Input - File name
    Output - List of Course objects
    """

    courses = open(file, 'r')
    course_list = []
    #iterates through the lines of the file
    for line in courses:
        line = line.strip() 
        values = line.split('\t') #course number, course name, pre-reqs, credits
        
        course_name = values[1]
        course_number = values[0]
        pre_reqs_spot = values[2][1:-1]
        pre_reqs_spot = pre_reqs_spot.replace(' ', '')
        pre_reqs_spot = pre_reqs_spot.strip()

        credits = float(values[3])
        
        pre_reqs = pre_reqs_spot.split(',')
        course = Course(course_name, course_number, pre_reqs, credits) #creates a course object
        course_list.append(course)
    return course_list

def find_class(course_list, number):
    """Function to find a course in the course list by course number
    Input - List of Course objects (all courses), course number
    Output - Course object or None
    """

    for course in course_list:
        #iterates through the list, checking each course number and returning the course object if it matches
        if course.course_number == number:
            return course
    return None #default if cannot find the course

def taken_courses(course_list):
    """Function to take in the courses the user has taken and return a list of Course objects
    Input - List of Course objects (all courses)
    User Input - course numbers
    Output - List of Course objects (courses taken)
    """

    print("Continue entering course numbers until you have entered all the courses you have taken. Once complete, type 'done'.")
    entering = True
    taken = []
    #continues asking for a course number until the user is done entering
    while entering:
        course = input("Enter the course number: ")
        course = course.strip()
        if course.isdigit() == False: #checks if the input is a number, if it is, they might be saying they are done
            user = input("Are you done entering courses? (y/n): ")
            if user == 'y': #if they are done, the loop ends
                entering = False
                break
            else: #else they made a mistake, give them a second chance
                course = input("Enter the course number: ")
        check = find_class(course_list, course)
        while check == None: #while the course is not in the list, ask for a new course
            print("Sorry, that course is not in our database.")
            course = input("Enter the course number: ")
            if course.isdigit() == False: #checks if the input is a number, if it is, they might be saying they are done
                user = input("Are you done entering courses? (y/n): ")
                if user == 'y': #if they are done, the loop ends
                    entering = False
                    break
                else: #else they made a mistake, give them a second chance
                    course = input("Enter the course number: ")
            check = find_class(course_list, course)

        if check not in taken: #stops duplicates
            if check != None: #stops the program from crashing if the course is not in the list
                taken.append(check)
    return taken

def eligible_courses(course_list, taken):
    """Function to find the courses the user is eligible to take based on the courses they have taken
    Input - List of Course objects (all courses), List of Course objects (courses taken)
    Output - List of Course objects (courses eligible to take)
    """
    eligible = []
    #loops through the courses in the course list
    for course in course_list:
        prerequisites = course.pre_reqs #gets the prerequisites for the course
        elig_flag = True
        #loops through the prerequisites for the course
        for prereq in prerequisites:
            if prereq == "":    #if there are no prerequisites, the course is eligible
                continue
            else:
                if prereq[-1] == 'c':   #if the prerequisite is concurrent, the course is eligible
                    prereq = prereq[:-1]
                prereq_course = find_class(course_list, prereq)
                if prereq_course not in taken:  #if the prerequisite is not in the taken list, the course is not eligible and the flag is changes
                    elig_flag = False
                    continue
        if elig_flag:   #if the flag is unchanged, it is added to the eligible list
            eligible.append(course)

    iter_list = eligible.copy()
    #removes courses that are already taken
    for eli_course in iter_list:    
        if eli_course in taken:
            eligible.remove(eli_course)

    return eligible

def concurrent_courses (course_list, taken, eligible):
    """Function to find the concurrent courses the user is eligible to take based on the courses they have taken and are eligible to take
    Input - List of Course objects (all courses), List of Course objects (courses taken), List of Course objects (courses eligible to take)
    Output - List of Course objects (courses eligible to take concurrently), List of Course objects (eligible classes required to take with the concurrent courses)
    """
    concurrent_prereq = []
    #loops through the courses in the course list
    for course in course_list:
        #checks if the course has the concurrent flag
        if course.concurrent:
            prereqs = course.pre_reqs
            con_flags = [None]*len(prereqs)
            counter = 0
            c_list = []
            for prereq in prereqs:
                if prereq[-1] == 'c':
                    prereq = prereq[:-1]
                    prereq_course = find_class(course_list, prereq)
                    if prereq_course in eligible:
                        con_flags[counter] = True
                        c_list.append(prereq_course)
                    else:
                        con_flags[counter] = False
                else:
                    prereq_course = find_class(course_list, prereq)
                    if prereq_course in taken:
                        con_flags[counter] = True
                    else:
                        con_flags[counter] = False
                counter += 1
            if False not in con_flags:
                concurrent_prereq.append([course,c_list])
            
    iter_list = concurrent_prereq.copy()
    #removes courses that are already taken
    for i in range(len(iter_list)):    
        if iter_list[i][0] in taken:
            concurrent_prereq.remove(iter_list[i])
        if iter_list[i][0] in eligible:
            concurrent_prereq.remove(iter_list[i])

                
    return concurrent_prereq