class Employee:
    def __init__(self, name, age, salary, employee_id):
        self.name = name
        self.age = age
        self.salary = salary
        self.employee_id = employee_id

def sort_employees(employees, parameter):
    return sorted(employees, key=lambda x: getattr(x, parameter))

employees = [Employee('Ramu', 35, 50000, 1), Employee('Tejas', 30, 60000, 2), Employee('Abhi', 25, 70000, 3), Employee('Jaya', 32, 60000, 4)]
sorted_employees = sort_employees(employees, 'age')  # Change 'age' to 'name', 'salary' or 'employee_id' as needed
for employee in sorted_employees:
    print(employee.name, employee.age, employee.salary, employee.employee_id)

