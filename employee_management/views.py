from django.shortcuts import render

from employee_management.model.employee import Employee
# Create your views here.


def first_page(request):
    employee_list = []
    employee = Employee('sho', '784396', 'osaka', 'aichi')
    employee_2 = Employee('masaya', '76854789', 'osaka', 'kyoto')
    employee_list.append(employee)
    employee_list.append(employee_2)
    first_page_dict = {'employee_list':employee_list}
    return render(request, 'employee_management/first_page.html', first_page_dict)


def detail_page(request):
    detail_page_dict = {}
    return render(request, 'employee_management/detail_page.html', detail_page_dict)


def add_function(request):
    return render(request, 'employee_management/add_function.html')
