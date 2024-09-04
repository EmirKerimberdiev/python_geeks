class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce(self):
        status = "married" if self.is_married else "not married"
        print(f"Name: {self.fullname}, Age: {self.age}, Status: {status}")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def get_average_marks(self):
        if self.marks:
            total_marks = sum(self.marks.values())
            number_of_subjects = len(self.marks)
            return total_marks / number_of_subjects
        return 0

    def introduce(self):
        super().introduce()
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"Average Mark: {self.get_average_marks():.2f}")


class Teacher(Person):
    BASE_SALARY = 30000

    def __init__(self, fullname, age, is_married, years_of_experience):
        super().__init__(fullname, age, is_married)
        self.years_of_experience = years_of_experience

    def calculate_salary(self):
        bonus = max(0, (self.years_of_experience - 3) * 0.05 * self.BASE_SALARY)
        return self.BASE_SALARY + bonus

    def introduce(self):
        super().introduce()
        print(f"Years of Experience: {self.years_of_experience}")
        print(f"Calculated Salary: ${self.calculate_salary():,.2f}")


def create_students():
    students = [
        Student("Alice Smith", 14, False, {"history": 25, "math": 55, "english": 95}),
        Student("Bob Johnson", 16, False, {"history": 65, "math": 95, "english": 34}),
        Student("Charlie Brown", 19, False, {"history": 65, "math": 90, "english": 72})
    ]
    return students


# Creating and displaying teacher information
teacher = Teacher("John Doe", 45, True, 10)
teacher.introduce()

# Creating and displaying student information
students = create_students()
for student in students:
    print("\nStudent Information:")
    student.introduce()
