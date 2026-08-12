from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Employee, Department, Category, Position, Salary,Leave
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum





def add_employee(request):

    departments = Department.objects.all()
    positions = Position.objects.all()


    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        salary = request.POST['salary']
        experience = request.POST['experience']


        department = Department.objects.get(
            id=request.POST['department']
        )


        position = Position.objects.get(
            id=request.POST['position']
        )


        Employee.objects.create(

            name=name,
            email=email,
            mobile=mobile,
            department=department,
            position=position,
            salary=salary,
            experience=experience

        )


        return redirect('dashboard')



    context = {

        "departments": departments,

        "positions": positions

    }


    return render(
        request,
        "add_employee.html",
        context
    )

def dashboard(request):

    employees = Employee.objects.all()


    pending_leave = Leave.objects.filter(
        status="Pending"
    ).count()


    context = {

        "employees": employees,

        "total_employee": Employee.objects.count(),

        "active_employee": Employee.objects.count(),

        "departments": Department.objects.count(),

        "positions": Position.objects.count(),

        "pending_leave": pending_leave,

    }


    return render(
        request,
        "dashboard.html",
        context
    )



def delete_employee(request,id):

    employee = get_object_or_404(Employee,id=id)

    employee.delete()

    return redirect('dashboard')


def edit_employee(request,id):

    employee = get_object_or_404(Employee,id=id)

    departments = Department.objects.all()
    positions = Position.objects.all()


    if request.method == "POST":

        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.mobile = request.POST.get('mobile')
        employee.salary = request.POST.get('salary')
        employee.experience = request.POST.get('experience')

        employee.department_id = request.POST.get('department')
        employee.position_id = request.POST.get('position')

        employee.save()

        return redirect('employees')


    return render(
        request,
        "edit_employee.html",
        {
            "employee":employee,
            "departments":departments,
            "positions":positions
        }
    )



def employees(request):

    employees = Employee.objects.all()

    return render(
        request,
        "employees.html",
        {
            "employees": employees
        }
    )

from .models import Department


def departments(request):

    departments = Department.objects.all()

    return render(
        request,
        "departments.html",
        {
            "departments": departments
        }
    )

def add_department(request):

    departments = Department.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")

        if name:
            Department.objects.create(
                name=name
            )

        return redirect("add_department")

    return render(
        request,
        "add_department.html",
        {
            "departments": departments
        }
    )


def delete_employee(request,id):

    employee = Employee.objects.get(id=id)

    employee.delete()

    return redirect('employees')
    

def delete_department(request,id):

    department = Department.objects.get(id=id)

    department.delete()

    return redirect('departments')


def positions(request):

    positions = Position.objects.all()

    return render(
        request,
        "positions.html",
        {
            "positions": positions
        }
    )

# Add Position
def add_position(request):

    if request.method == "POST":

        name = request.POST.get("name")

        Position.objects.create(
            name=name
        )

        return redirect("positions")

    return render(request,"add_position.html")



def delete_position(request, id):

    position = Position.objects.get(id=id)

    position.delete()

    return redirect("positions")


def add_salary(request):

    employees = Employee.objects.all()

    if request.method == "POST":

        Salary.objects.create(
            employee_id=request.POST.get("employee"),
            month=request.POST.get("month"),
            amount=request.POST.get("amount")
        )

        return redirect("salaries")


    return render(request,"add_salary.html",{
        "employees":employees
    })


def delete_salary(request, id):

    salary = get_object_or_404(Salary, id=id)

    salary.delete()

    return redirect('salaries')


def salaries(request):

    salaries = Salary.objects.all()

    return render(request,"salaries.html",{
        "salaries": salaries
    })



def leaves(request):

    leave_data = Leave.objects.all()

    context = {
        "leaves": leave_data
    }

    return render(request, "leaves.html", context)

def add_leave(request):

    employees = Employee.objects.all()

    if request.method == "POST":

        employee_id = request.POST.get("employee")

        leave_type = request.POST.get("leave_type")
        days = request.POST.get("days")
        reason = request.POST.get("reason")


        Leave.objects.create(
            employee_id=employee_id,
            leave_type=leave_type,
            days=days,
            reason=reason,
            status="Pending"
        )


        return redirect("leaves")


    return render(
        request,
        "add_leave.html",
        {
            "employees": employees
        }
    )

def delete_leave(request,id):

    leave = Leave.objects.get(id=id)

    leave.delete()

    return redirect("leaves")


def reports(request):

    employees = Employee.objects.all()

    context = {
        "employee_count": employees.count(),
        "department_count": Department.objects.count(),
        "total_salary": employees.aggregate(
            total=Sum('salary')
        )['total'] or 0,

        "employees": employees,
    }

    return render(request, "reports.html", context)



def settings(request):
    return render(request,"settings.html")



def home(request):
    return render(request, 'home.html')
   

def about(request):
    return render(request, 'about.html')


def employee_register(request):

    if request.method == "POST":

        return redirect('employee_login')


    return render(request, 'employee_register.html')

def admin_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request, user)

            return redirect('dashboard')


        else:

            messages.error(request, "Invalid Username or Password")


    return render(request, "login.html")
    

def admin_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request, user)

            return redirect("dashboard")


        else:

            return render(request,"login.html",{
                "error":"Invalid Username or Password"
            })


    return render(request,"login.html")


def employee_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(request, user)

            return redirect("dashboard")


        else:

            messages.error(request, "Invalid Username or Password")


    return render(request, "employee_login.html")


@login_required
def edit_profile(request):

    user = request.user


    if request.method == "POST":

        user.username = request.POST.get("name")
        user.email = request.POST.get("email")

        user.save()


        return redirect("settings")


    return render(request,"edit_profile.html",{
        "user":user
    })


def update_settings(request):

    if request.method == "POST":

        website_name = request.POST.get("website_name")

        print("Updated Website Name:", website_name)

        return redirect("settings")


    return render(request,"update_settings.html")

@login_required
def employee_dashboard(request):
    return render(request, "employee_dashboard.html")






