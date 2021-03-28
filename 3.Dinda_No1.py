class Employee:
    types = "Employees"
    def __init__(self, name, job_role):
        self.name = name  
        self.job_role = job_role

    def working(self) : 
        print(self.name, "is a", self.job_role)

    @classmethod
    def salary(cls):
        print(cls.types, "get salary")

class Engineer(Employee):
    types = "Full time employee"
    def working(self):
        print(self.name, "working as a", self.job_role)
    
    def mealAllowance(self, meal = None):
        if meal == None:
            print(self.name, "Not get meal allowance")
        else :
            print(self.name, "eat", meal, "during break")

Dinda = Employee("Dinda", "Programmer")
Dindu = Engineer("Dindu", "Data Engineer")
Dinda.salary()
Dinda.working()
print("")
Dindu.salary()
Dindu.working()
Dindu.mealAllowance()
Dindu.mealAllowance("pizza")



    

    

