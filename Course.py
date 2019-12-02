class Course(object):
    def __init__(self, course):
        self.course = course

    # get course
    def getCourse(self):
        return self.course

    # check course avalilability
    def checkCourse(self):
        for index in range(len(self.course)):
            if len(self.course) <= 15:
                return True
            else:
                return False