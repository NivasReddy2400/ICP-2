class Employee:
    employee_count = 0
    total_salary = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.employee_count += 1
        Employee.total_salary += salary

    @staticmethod
    def average_salary():
        if Employee.employee_count == 0:
            return 0
        return Employee.total_salary / Employee.employee_count

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Family: {self.family}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department, benefits):
        super().__init__(name, family, salary, department)
        self.benefits = benefits

    def display_info(self):
        super().display_info()
        print(f"Benefits: {self.benefits}")

emp1 = Employee("Rick", "Grimes", 999999, "HR")
emp2 = Employee("Negan", "Smith", 900000, "PR")
fulltime_emp1 = FulltimeEmployee("Daryl", "Dixon", 20000, "Sales", "Health Insurance")

print("Employee 1 Information:")
emp1.display_info()
print("\nEmployee 2 Information:")
emp2.display_info()
print("\nFulltime Employee 1 Information:")
fulltime_emp1.display_info()

print("\nAverage Salary of Employees:")
print(Employee.average_salary())
