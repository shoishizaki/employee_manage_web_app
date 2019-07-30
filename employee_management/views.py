from django.shortcuts import render

from employee_management.model.employee_model import Employee
# Create your views here.


def first_page(request):
    employee_list = Employee.objects.all()
    first_page_dict = {'employee_list':employee_list}
    return render(request, 'employee_management/first_page.html', first_page_dict)


def detail_page(request):
    detail_page_dict = {}
    return render(request, 'employee_management/detail_page.html', detail_page_dict)


def add_function(request):
    return render(request, 'employee_management/add_function.html')
