#initiate a class.
class Employee:
    #special method / dunder method /magic method / constructor
    def __init__(self,name,age,salary,designation):
        self.name = name
        self.age = age
        self.salary = salary
        self.designation = designation

    def display(self):#like in java this is implict . here self is explicit 
        print(f"Name: {self.name} Age: {self.age} Salary: {self.salary} Designation: {self.designation}")

    def doplayCricket(self):
        if(self.age > 18 and self.salary > 50000):
            print(f"{self.name} can play cricket")


emp1 = Employee("Aakash",22,100000,"MLOPs Engineer")

emp1.display()
emp1.doplayCricket()
emp2 = Employee("Bhuvan",22,100000,"SDE")
print(emp1,emp2)



















"""
    name,age,salary = "","",0 

    class variables and we need to initiate them with some values. Also
     we can't use self keyword here. because self is used to access instance variables.

    making new data attribures from object level is not a good practice. because
    it will create new data attributes for each object. so we need to initiate them in constructor.


    sam = Employee()
    sam.name = "Sam"
    sam.age = 25
    sam.salary = 50000
    sam.height = 6.6
    print(sam.name ,sam.age,sam.salary,sam.height)

    ram = Employee()
    ram.name = "ram"
    ram.age = 25
    ram.salary = 50000
    #ram.height = 6.6
    print(ram.name ,ram.age,ram.salary,ram.height)

    2.Second trail
    class Employee:

    def __init__(self):
        self.name = "Sam"
        self.age = 25
        self.salary = 50000

    sam = Employee()
    print(f"Name: {sam.name} Age: {sam.age} Salary: {sam.salary}")

    ram = Employee()
    print(f"Name: {ram.name} Age: {ram.age} Salary: {ram.salary}")
    """