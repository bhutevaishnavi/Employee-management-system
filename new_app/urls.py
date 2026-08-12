from django.urls import path
from . import views


urlpatterns = [

    # path('', views.dashboard, name="dashboard"),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),

    path('employees/', views.employees, name="employees"),

    path('departments/', views.departments, name="departments"),
     path("add-department/", views.add_department, name="add_department"),

    path('positions/', views.positions, name="positions"),
    path('add_position/', views.add_position, name='add_position'),
    path('delete_position/<int:id>/', views.delete_position,name='delete_position'),

    path('salaries/', views.salaries, name="salaries"),

    path('leaves/', views.leaves, name="leaves"),

    path('reports/', views.reports, name="reports"),

    path('add_employee/', views.add_employee, name="add_employee"),

    path('edit_employee/<int:id>/', views.edit_employee, name="edit_employee"),

    path('delete_employee/<int:id>/', views.delete_employee, name="delete_employee"),

    path('salaries/', views.salaries, name="salaries"),

    path( 'add-salary/', views.add_salary, name="add_salary"),
    path( 'delete-salary/<int:id>/', views.delete_salary, name="delete_salary"),

    path('leaves/', views.leaves, name='leaves'),

    path('add-leave/', views.add_leave, name='add_leave'),
    path( 'delete-leave/<int:id>/', views.delete_leave, name="delete_leave"),

    path('reports/', views.reports, name="reports"),

    # path('settings/', views.settings, name="settings"),

    path(  "delete-department/<int:id>/",  views.delete_department,  name="delete_department"),
    path('login/', views.admin_login, name='login'),

    path('employee-login/', views.employee_login, name='employee_login'),

    path('register/', views.employee_register, name='employee_register'),

    path('settings/', views.settings, name="settings"),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('update-settings/', views.update_settings, name='update_settings'),

    path( 'employee-dashboard/', views.employee_dashboard, name='employee_dashboard'),

]