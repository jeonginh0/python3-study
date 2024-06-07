# Oop3.py

class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print("저의 이름은", self.name, "이고, 제 나이는", str(self.age), "살입니다.")

class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date

    def do_work(self):
        print("일을 열심히 한다")

    def do_coding(self):
        print("열심히 코드를 작성한다")

    def about_me(self):
        super().about_me()
        print("제 급여는", self.salary, "원 이고, 제 입사일은", self.hire_date, "입니다.")

Inho1 = Person("Inho Jeong",24, 'Male')
Inho1.about_me()
print(Inho1.name, Inho1.age, Inho1.gender)
print("--------------------------------------------------")

Inho = Employee("Inho Jeong",24, 'Male', "개발자", '2026')
Inho.do_coding()
Inho.about_me()
print(Inho.name, Inho.age, Inho.gender, str(Inho.salary), str(Inho.hire_date))