# OOP1 - 객체지향 프로그래밍

class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print("저의 이름은", self.name, "이고,", self.age, "살 이며,", self.gender," 입니다.")

class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super(Employee, self).__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date

p1 = Person('jung', 45, 'M')
print(p1.age)

e1 = Employee('zhang', 24, 'M', "학생", 2001)
print(e1.age)