from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    taskTitle = models.CharField(max_length=300)
    taskDesc = models.TextField()
    # taskDate = models.DateField()

    time= models.DateTimeField(auto_now_add=True)

class Register(models.Model):
    first_name =models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    username = models.CharField(max_length=300)
    password1 = models.CharField(max_length=300)
    password2 = models.CharField(max_length=300)
    email = models.CharField(max_length=300)

class login(models.Model):
    username = models.CharField(max_length=300)
    password1 = models.CharField(max_length=300)



    def __str__(self):
        return self.taskTitle
    def __str__(self):
        return self.email
    def __str__(self):
        return self.username