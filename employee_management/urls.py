from django.urls import path

from . import views

urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('detail/', views.detail_page, name='detail_page'),
    path('add/', views.add_function, name='add'),
]
