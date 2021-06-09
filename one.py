#class - template has variables that represent an object & functions that munipulate the variables
# every class has a constructor which initialize variables of the object

class Employee:
    #Constructor willl initialize a new object 
    def __init__(self, n, s, bank): # __ just for init
        self.name = n
        self.salary = s
        self.b = bank
        # self is object

    def get_raise(self, moony): #this is method/function manipulating evil BUT USE METHODS IN JAVA
        self.salary += moony

    def get_broke(self, woomp):
        self.salary -= woomp



emp1 = Employee("Rebecca", 1000, 9999999999)
emp2 = Employee("Mike", 0.5, 1)
emp3 = Employee("Scooby", 1, 2)

# dot notation: access variables of an object. objects are things created from the class like emp1     

print(emp1.salary) #yeesh

emp1.get_raise(20)
print(emp1.salary)

emp1.get_broke(40)
print(emp1.salary)



class Employer:
    def __init__(self, company_name, shmoney):
        self.cn = company_name
        self.s = shmoney
        self.p = [] #empty list
        
    def add_employee(self, employee_name):
        # an array is a list in python.
        self.p.append(employee_name)

    def pay_employees(self):
        for i in range(len(self.p)): #could do 3 as well but not good
            self.p[i].b += 20 # bad v bad do one below
             p[i].get_raise(20)


big_boss = Employer("Greg", 10)
small_boss = Employer("Steve", 10000000000)

big_boss.add_employee(emp2)
big_boss.add_employee(emp1)
big_boss.add_employee(emp3)


print(big_boss.p[0].name)
big_boss.pay_employees()
print(emp1.b)

