class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade
    
    
class Course:
    def __init__(self, name, max_students, gpa):
        self.name = name
        self.max_students = max_students
        self.gpa = gpa
        self.students = []
        
    # add students to the course if their gpa is higher than recommended and space is enough
    def add_students(self, student):
        if student.grade >= self.gpa and len(self.students) < self.max_students:
            self.students.append(student)
            print("success, student is added")
        else:
            print("the course is full")
            
s1 = Student("John", 21, 75)
s2 = Student("Bill", 22, 80)

course1 = Course("Maths", 3, 76)
course1.add_students(s2)