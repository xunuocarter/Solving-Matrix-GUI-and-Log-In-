"""
This project will help college students to solve the most important part,
which is Derivative, math questions. Students need to log in first,
then they can type in the questions that they have. Finally, students will
have the correct answer after click the "compute" button. Students can
type in as much questions as they have. At last, students need to log out
for finishing the project.
"""

from Student import Student
from Course import Course
from Calculate import Calculate
from tkinter import *

class LogIn(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Welcome to Derivitive!")
        self.grid()
        self.master.geometry("700x500")


        #Name Label
        self._NameLabel = Label(self,text = "Name")
        self._NameLabel.grid(row = 0, column = 0, sticky = W)
        self._NameVar = StringVar()
        self._NameEntry = Entry(self, textvariable = self._NameVar)
        self._NameEntry.grid(row = 0, column = 1, columnspan = 3)

        #ID Label
        self._IdLabel = Label(self, text = "ID")
        self._IdLabel.grid(row = 1, column = 0, sticky = W)
        self._IdVar = StringVar()
        self._IdEntry = Entry(self, textvariable = self._IdVar)
        self._IdEntry.grid(row = 1, column = 1, columnspan = 3)

        #Course Label
        self._CourseLabel = Label(self, text = "Course")
        self._CourseLabel.grid(row = 2, column = 0, sticky = W)
        self._CourseVar = StringVar()
        self._CourseEntry = Entry(self, textvariable = self._CourseVar)
        self._CourseEntry.grid(row = 2, column = 1, columnspan = 3)

        #Blank Labels
        self._BlankLabel = Label(self, text = "")
        self._BlankLabel.grid(row = 3,column = 0)
        self._BlankLabel = Label(self, text="")
        self._BlankLabel.grid(row=4, column=0)
        self._BlankLabel = Label(self, text="")
        self._BlankLabel.grid(row=5, column=0)
        self._BlankLabel = Label(self, text="")
        self._BlankLabel.grid(row=7, column=0)
        self._BlankLabel = Label(self, text="")
        self._BlankLabel.grid(row=9, column=0)

        #Answer Label
        self._AnswerLabel = Label(self, text = "Answer")
        self._AnswerLabel.grid(row = 10, column = 0, sticky = W)
        self._AnswerVar = StringVar()
        self._AnswerEntry = Entry(self, width = 35, textvariable = self._AnswerVar)
        self._AnswerEntry.grid(row = 10, column = 1)

        #Problem Label
        self._ProblemLabel = Label(self, text = "Problem")
        self._ProblemLabel.grid(row = 6, column = 0, sticky = W)
        self._ProblemVar = StringVar()
        self._ProblemEntry = Entry(self, width = 35, textvariable = self._ProblemVar)
        self._ProblemEntry.grid(row = 6, column = 1)

        #Status Label
        self._outputArea = Text(self, width = 18, height = 15, wrap = WORD)
        self._outputArea.grid(row = 1, column = 16, columnspan = 2)
        self._StatusLabel = Label(self, text = "Status")
        self._StatusLabel.grid(row = 1, column = 15)
        self._outputArea.insert("1.0", "Please Log In first.")


        #Log In Button
        self._LoginButton= Button(self, height = 2, width = 7,text = "Log in", command = self._login)
        self._LoginButton["state"] = NORMAL
        self._LoginButton.grid(row = 1, column = 4)

        #Compute Button
        self._ComputeButton = Button(self, text = "Compute", command = self._compute)
        self._ComputeButton["state"] = DISABLED
        self._ComputeButton.grid(row = 8, column = 1)

        #Clear Button
        self._ClearButton = Button(self, text = "Clear", command = self._clear)
        self._ClearButton["state"] = DISABLED
        self._ClearButton.grid(row = 8, column = 2)




    #login button command
    def _login(self):
        name = self._NameVar.get()
        id = self._IdVar.get()
        course = self._CourseVar.get()
        self.student = Student(name, id)   #inheritance from Students class
        self.course = Course(course)       #inheritance from Course class
        if self.student.checkName():
            if self.course.checkCourse():
                self._outputArea.delete("1.0", END)     # for texts
                self._outputArea.insert("1.0", "Log in successfully!\n"
                                               "\n"
                                               "No space between characters.\n"
                                               "\n"
                                               "No need to type f(x)= or y=.\n"
                                               "\n"
                                               "For Example: sin(x^23)+6x.")
                self._ComputeButton["state"] = NORMAL
                self._ClearButton["state"] = NORMAL
                self._LoginButton["text"] = "Log out"   # log in and log out exchange
                self._LoginButton["command"] = self._logout
            else:
                self._outputArea.delete("1.0", END)
                self._outputArea.insert("1.0", "Invalid log in information! Please enter again.")
        else:
            self._outputArea.delete("1.0", END)
            self._outputArea.insert("1.0", "Invalid log in information! Please enter again.")

    #compute button command
    def _compute(self):
        equation = self._ProblemVar.get()    # get the question
        self.calculate = Calculate(equation)    #inheritance from Calculate class
        if self.calculate.compute():         # calculate
            self._AnswerVar.set(self.calculate.result)   # set to GUI
        else:
            self._outputArea.delete("1.0", END)
            self._outputArea.insert("1.0", "Invalid Equation input. Please enter again.\n"
                                           "\n"
                                           "No space between characters.\n"
                                            "\n"
                                            "No need to type f(x)= or y=.\n"
                                            "\n"
                                            "For Example: sin(x^23)+6x.")
    # clear button command
    def _clear(self):
        self._ProblemVar.set("")
        self._AnswerVar.set("")

    # log out button command
    def _logout(self):
        self._outputArea.delete("1.0", END)
        self._outputArea.insert("1.0", "Log out successfully!\n"
                                       "\n"
                                       "Please Log in first.")
        self._ProblemVar.set("")
        self._AnswerVar.set("")
        self._ComputeButton["state"] = DISABLED
        self._ClearButton["state"] = DISABLED
        self._LoginButton["text"] = "Log In"    # log in and log out exchange
        self._NameVar.set("")
        self._IdVar.set("")
        self._CourseVar.set("")
        self._LoginButton["text"] = "Log in"
        self._LoginButton["command"] = self._login


def main():
    LogIn().mainloop()
main()