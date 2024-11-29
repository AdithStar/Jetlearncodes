class Student:
    name = " "
    age = 12
    Class = "Grade 5" 
    house = "Ruby"
    class_teacher = "Bhavana"
    
    def  __init__(self):
        print("creating a new student")


    def change_details(self,age):
        print("please enter your age")
        self.age = int(input())
        print("please enter your name")
        self.name = input()
    

    def show_details(self):
        print("The details of student are")
        print(self.name)
        print(self.house)
        print(self.Class)
        print(self.age)
        print(self.class_teacher)

Adith = Student()
Adith.change_details
Adith.show_details()
    
