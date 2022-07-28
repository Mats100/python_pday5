class Student:
    def GetStudentInfo(self):
        self.__rollno = input("Enter Roll Number: ")
        self.__name = input("Enter Name: ")
        self.__physics = int(input("Enter Physics Marks: "))
        self.__chemistry = int(input("Enter Chemistry Marks: "))
        self.__maths = int(input("Enter Math Marks: "))
    def printResult(self):
        print(self.__rollno,self.__name, ((int)( (self.__physics+self.__chemistry+self.__maths)/300*100 )))

Student_Array = []

while True:
    student = Student()
    student.GetStudentInfo()
    Student_Array.append(student)
    choice = input("Add More y/n?")
    if choice == 'n':
        break
print("Results : ")
for Student in Student_Array:
    student.printResult()
