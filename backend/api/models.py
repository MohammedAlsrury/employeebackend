from django.db import models

class Department(models.Model):
    department_name = models.CharField( max_length=50)



class Employees(models.Model):
    employees_name = models.CharField( max_length=50)
    image = models.ImageField( upload_to='photo/%y/%m/%d',)
    trianing = models.BooleanField(default= False)
    age = models.IntegerField()
    phone =models.CharField(max_length =20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    join_date = models.DateTimeField( auto_now_add=True)


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    descripe =models.TextField()
    employees = models.ForeignKey(Employees,  on_delete=models.CASCADE)
    
    
class Achivment(models.Model):
    employees= models.ForeignKey(Employees, on_delete=models.CASCADE)
    date = models.DateTimeField( auto_now_add=True)
    achivment =models.CharField( max_length=50) 