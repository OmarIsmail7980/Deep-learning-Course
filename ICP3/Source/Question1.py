
class Employee:
    #store sum and salary of emp
    emp_num = 0
    total_salary = 0
    
    def __init__(self,n,f,s,dept):
      self.name = n
      self.family = f
      self.salary = s
      self.department = dept
      
      Employee.total_salary = Employee.total_salary + self.salary
      Employee.emp_num = Employee.emp_num+1
      
    def avg(self):
        result = Employee.total_salary/Employee.emp_num
        return result
            
    
    
    
class Full_Emp(Employee):
    
    def __init__(self,n,f,s,dept):
        Employee.__init__(self,n,f,s,dept)
        
    def avg(self):
        Employee.avg(self)



s = Employee("man", "many", 12000, "IT")

m = Full_Emp("man", "many", 12000, "medical")

s = Employee("man", "many", 1227876, "Engineering")

print("\nThe Average of the employees salary is: ", s.avg())


        
