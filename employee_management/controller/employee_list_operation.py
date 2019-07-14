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
        for i in range(len(employee_list)):
            print('ID:', i, employee_list[i])


    def delete_employee(self, employee_list):
        while True:
            if len(employee_list) == 0:
                print('There is no data to delete.')
                break

            else:
                print('Please choose delete ID.')
                self.show_employee(employee_list)
                number = input('ID:')
                if int(number) <= len(employee_list) - 1:
                    del employee_list[int(number)]
                    break

                else:
                    print('This number is not define.')
                    break

    def update_employee(self, employee_list):
        while True:
            if len(employee_list) == 0:
                print('There is no data to update.')
                break

            else:
                print('Please choose update ID.')
                self.show_employee(employee_list)
                number = input('ID:')
                if int(number) <= len(employee_list) - 1:
                    print('Please write The information.')
                    name = input('Name:')
                    phone = input('Phone:')
                    home = input('Home:')
                    address = input('Address:')
                    self.employee_list[int(number)].set_name(name)
                    self.employee_list[int(number)].set_phone(phone)
                    self.employee_list[int(number)].set_home(home)
                    self.employee_list[int(number)].set_address(address)
                    break

                else:
                    print('This number is not define.')
                    break