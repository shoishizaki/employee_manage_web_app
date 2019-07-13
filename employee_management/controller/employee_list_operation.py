import employee_management.model.employee

class Employee_list_operation():
    def __init__(self):
        self.employee_list = []


    def add_employee(self):
        print('Please write your information.')
        name = input('Name:')
        phone = input('Phone:')
        home = input('Home:')
        address = input('Address:')
        emp = employee_management.model.employee.Employee(name, phone, home, address)
        self.employee_list.append(emp)


    def show_employee(self, employee_list):
        for employee in employee_list:
            print(employee)