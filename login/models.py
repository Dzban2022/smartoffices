from django.db import models

# Create your models here.
class Project(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField()
    project =models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.project.name

class User(models.Model):
    User = models.CharField(max_length = 200)
    Nombre = models.CharField(max_length = 200)
    Correo = models.CharField(max_length = 200)

def __str__(self):
        return 'Your user is: % % % %' %(self.User, self.Nombre, self.Correo)