# Best practice of naming classes in python is UpperCamelCase (without underscore)
class Student:
    # Constructor
    def __init__(self,name,exam):
        # 'self' reference to class instance
        self.name = name #property or attribute
        self.exam = exam

    # method
    def info(self):
        return f"Student Name: {self.name}, exam: {self.exam}"
    def passthrough(self):
        print(f"{self.name} was successfull") if self.exam >=70 else print(f"{self.name} was failed")
        return

# make an object from class
reindhart = Student("Reindhart",80)
print(reindhart.name)
print(reindhart.exam)
print(reindhart.info())
dumbass = Student("Dumbass",50)
dumbass.passthrough()


# ---------------------------------------------------------------------------------------------
class SuperStudent:
    school_name = "Sekolah Bahasa Ular"
    total_students = 0

    def __init__(self,name,exam):
        self.name = name
        self.exam = exam
        SuperStudent.total_students +=1

    # general method
    def info(self):
        return f"Super Student Name: {self.name}, Exam: {self.exam}"
    # Static Method ('self' not required)
    @staticmethod
    def get_school():
        return SuperStudent.school_name
    # Class Method (accepts params/args) and not mentioning the name of class
    @classmethod
    def super_student_intotal(cls, params):
        if params not in ["terbaik"]:
            return f"Total students in {cls.school_name} was {cls.total_students}. {params}"
        else :
            return f"Total strudents in {cls.school_name} was {cls.total_students}. {params}"

    # Property decorator --> give method access like property
    @property
    def status(self):
        if self.exam >= 90:
            return  f"{self.name} has Exam Grade : A"
        elif self.exam >=80:
            return f"{self.name} has Exam Grade : B"
        else:
            return f"{self.name} has Exam Grade : C"

andi = SuperStudent("Andi",85)
budi = SuperStudent("Budi",90)
joko = SuperStudent("Joko", 60)

print(SuperStudent.super_student_intotal("terburuk"))
print(joko.status)
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# inheritence
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"Name: {self.name}, Age: {self.age}"
# child class
class Employee(Person):
    def __init__(self,name,age,company_name):
        # call parent constructor
        super().__init__(name,age)
        self.company_name = company_name
    # overriding parent method
    def info(self):
        # using parent method
        person_info = super().info()
        return f"{person_info}, Employeed at: {self.company_name}"

deindara = Employee("Deindara",21,"Hyundai E&C")
print(deindara.info())
# ----------------------------------------------------------------------------------------------

# Private Variable , pass syntax & encapsulation OOP
class BankAccount:
    def __init__(self,name,balance,pin):
        self.__name = name  # Private variable (__), common used to read-only variable, will bypass Setter function
        self.balance = balance
        self.pin = pin

    # Encapsulation in OOP (always using private variable)
    # Getter
    @property
    def balance(self):
        return self.__balance
    # Setter
    @balance.setter
    def balance(self, value):
        if value >0:
            self.__balance = value
        else:
            self.__balance = f"Your Account was EMPTY!!!"
    @property
    def pin(self):
        if isinstance(self.__pin,str):
            return self.__pin
        return "*****"
    @pin.setter
    def pin(self,value):
        if len(str(value)) == 6:
            self.__pin = value
        else:
            self.__pin = "PIN Must Be 6 Digit"

class Bca(BankAccount):
    pass  # pass syntax to markable as empty inheritence class

bca_account = Bca("Andi",0,1234)
print(bca_account.balance)
print(bca_account.pin)

