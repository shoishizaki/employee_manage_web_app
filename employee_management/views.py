from django.shortcuts import render
from django.shortcuts import redirect

from employee_management.model.employee_model import Employee
from .forms import AddForm
# Create your views here.


def first_page(request):
    employee_list = Employee.objects.all()
    first_page_dict = {'employee_list':employee_list}
    return render(request, 'employee_management/first_page.html', first_page_dict)


def detail_page(request):
    detail_page_dict = {}
    return render(request, 'employee_management/detail_page.html', detail_page_dict)


def add_page(request):
    form = AddForm(request.POST or None)
    employee_list = Employee.objects.all()
    add_page_dict = {'employee_list': employee_list, 'form':form}
    if form.is_valid():
        employee = Employee()
        employee.name = form.cleaned_data['name']
        employee.phone = form.cleaned_data['phone']
        employee.home = form.cleaned_data['home']
        employee.address = form.cleaned_data['address']

        Employee.objects.create(
            name=employee.name,
            phone=employee.phone,
            home=employee.home,
            address=employee.address,
        )
        return redirect('first_page')
    return render(request, 'employee_management/add_function.html', add_page_dict)


def delete_page(request, pk):
    date = Employee.objects.get(pk=pk)
    date.delete()
    return redirect('first_page')