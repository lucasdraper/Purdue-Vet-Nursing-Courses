class Course:
    """A Class to contain course information"""
    def __init__(self, course_name, course_number, pre_req_list, credits):
        self.course_name = course_name
        self.course_number = course_number
        self.pre_reqs = []
        self.credits = credits
        self.concurrent = False

        #Checks if the course is able to be taken concurrently and creates a list of prerequisites, removing the c where applicable
        for i in range(len(pre_req_list)):
            cur = pre_req_list[i]
            if cur == '':
                continue
            if cur[-1] == 'c':
                self.concurrent = True    
            self.pre_reqs.append(cur)
