from django.db import models

# Create your models here.

class Role(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    role= models.ForeignKey(Role,on_delete=models.CASCADE)

    def __str__(self):
        return self.username