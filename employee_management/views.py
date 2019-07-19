from django.shortcuts import render
# Create your views here.

def first_page(request):
    first_page_dict = {}
    return render(request, 'employee_management/first_page.html', first_page_dict)

def detail_page(request):
    detail_page_dict = {}
    return render(request, 'employee_management/detail_page.html', detail_page_dict)
