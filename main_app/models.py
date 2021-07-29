from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    insurance = models.CharField(max_length=255)
    address = models.TextField()
    underlying_conditions = models.TextField()

    def __str__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length=255)
    opening = models.IntegerField()
    closing = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Vaccine(models.Model):
    name = models.CharField(max_length=255)
    opening = models.IntegerField()
    closing = models.IntegerField()
    address = models.TextField()
    vaccines = models.CharField(max_length=200)
    appointments = models.DateField()

    def __str__(self):
        return self.name

class Vaccinating(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=1, related_name='pvaccinating')
    site = models.ForeignKey(Vaccine, on_delete=models.CASCADE, default=1, related_name='svaccinating')


class Testing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=1, related_name='ptesting')
    site = models.ForeignKey(Test, on_delete=models.CASCADE, default=1, related_name='stesting')