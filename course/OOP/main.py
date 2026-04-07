# print(type("hello"))

class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Tim", 23)

# print(Dog("RAMA", 9).get_name())
# # print(Dog("RAMA", 9).get_age())
# d.set_age(12)
# print(d.get_age())

# More descriptive example OOP


class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course():
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avarage_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

    def get_all_student(self):
        allStudent = []
        for s in self.students:
            allStudent.append(s)
        print(len(allStudent))
        return allStudent


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
# print(course.students[1].name)
# print(course.get_avarage_grade())
# print(course.get_all_student())


# Inheritance

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what to say.")


class Cat(Pet):
    # when we want to add some parameter on the single class not parent one
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(
            f"I am {self.name} and I am {self.age} years old and I am {self.color}.")


class Dog(Pet):
    def __init__(self, name, age, genre):
        super().__init__(name, age)
        self.genre = genre

    def speak(self):
        print("Bark")

    def show(self):
        print(
            f"I am {self.name} and I am {self.age} years old and my genre is {self.genre}.")


class Fish(Pet):
    pass


# p = Pet("Tim", 19)
# p.show()
# c = Cat("Bill", 18, "Gray")
# c.show()
# c.speak()
# d = Dog("Jill", 23, "Shepard")
# d.show()
# d.speak()
# f = Fish("Bubble", 10)
# f.speak()


# CLASS ATTRIBUTES

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        # Person.number_of_people += 1
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Tim")
p2 = Person("Jim")
p3 = Person("Bummy")
p3 = Person("yummy")
print(Person.number_of_people_())
