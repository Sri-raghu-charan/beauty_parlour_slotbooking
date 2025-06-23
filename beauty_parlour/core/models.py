from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    specialization = models.ManyToManyField(Service)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ])

    def __str__(self):
        return f"{self.customer.name} - {self.service.name} at {self.appointment_time}"

# Create your models here.
