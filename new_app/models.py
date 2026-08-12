from django.db import models
from django.utils import timezone



class Category(models.Model):

    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name



class Department(models.Model):

    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name



class Position(models.Model):

    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Employee(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    mobile = models.CharField(max_length=15)


    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


    salary = models.IntegerField()

    experience = models.IntegerField(default=0)



    def __str__(self):
        return self.name


class Leave(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    leave_type = models.CharField(
        max_length=100,
        default="Casual Leave"
    )

    days = models.IntegerField(
        default=1
    )

    reason = models.CharField(
        max_length=200
    )

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    date = models.DateField(
        default=timezone.now
    )


    def __str__(self):
        return self.employee.name

# class Leave(models.Model):

#     employee = models.ForeignKey(
#         Employee,
#         on_delete=models.CASCADE
#     )

#     reason = models.CharField(max_length=200)

#     status = models.CharField(
#         max_length=20,
#         default="Pending"
#     )

#     date = models.DateField(
#         default=timezone.now
#     )


class Salary(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="salary_details"
    )

    month = models.CharField(max_length=50)

    amount = models.IntegerField()


    def __str__(self):
        return self.employee.name