class Student:

    # static variables
    sno=0
    dept="CSE"
    college="REC"

    def __init__(self,name,rno,cgpa):
        self.name=name
        self.rno=rno
        self.cgpa=cgpa
        Student.sno+=1
        print("S.No:",Student.sno)
        self.display()

    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.rno)
        print("Department:",Student.dept)
        print("College:",Student.college)
        print()

    @staticmethod
    def getCollege():
        print(Student.college)

s1=Student("Santhosh",233,8.16)
s2=Student("Ram",207,7.8)
s3=Student("Senthil",238,9.0)

s1.getCollege()
Student.getCollege()
