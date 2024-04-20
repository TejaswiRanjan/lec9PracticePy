#Define a Employee class with attributes role,department & salary . This class has also a show Details() method.

#Create an Engineer class that inherits property from Employee & has aditional attributes : name & age

class Employee:

    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):

        print("Role = ",self.role)
        print("Department = ",self.department)
        print("Salary = ",self.salary)


class Engineer(Employee):

    def __init__(self,name,age):

        self.name = name
        self.age = age
        super().__init__("Software_engineer","Development",100000)

    def showDetails(self):

        print("Role = ",self.role)
        print("Department = ",self.department)
        print("Salary = ",self.salary)
        print("Name = ",self.name)
        print("Age = ",self.age)

en1 = Engineer("Tejaswi_Ranjan",21)
en1.showDetails()
        