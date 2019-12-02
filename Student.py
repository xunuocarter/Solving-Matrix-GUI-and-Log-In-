class Student(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # get name
    def getName(self):
        return self.name
    # get id
    def getId(self):
        return self.id

    # check name and id availability
    def checkName(self):
        for index in range(len(self.name)):
            if not self.name[index].isalpha():
                return False
        for i in range(len(self.id)):
            if not self.id[i].isdigit() or len(self.id) > 8:
                return False

        return True

