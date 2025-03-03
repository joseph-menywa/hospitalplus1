from django.db import models
from django.forms.fields import CharField


# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()


    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age =  models.IntegerField()
    email = models.EmailField()
    department = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class staff(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Position = models.CharField(max_length=20)
    Phonenumber = models.CharField(max_length=10)
    Email = models.EmailField()
    Hiredate = models.DateField()

    def __str__(self):
        return self.Firstname + ""+ self.Lastname

class Ward(models.Model):
    Name = models.CharField(max_length=50)
    Totalbeds = models.IntegerField()
    Availablebeds = models.IntegerField()


    def __str__(self):
        return self.Name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone  = models.CharField(max_length=100)
    date = models.DateTimeField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject  = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


