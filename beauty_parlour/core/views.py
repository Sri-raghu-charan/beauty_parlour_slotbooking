from django.shortcuts import render, redirect
from .models import Appointment, Customer
from .forms import AppointmentForm, CustomerForm
from django.contrib import messages


def home(request):
    # Show all appointments
    appointments = Appointment.objects.all().order_by('-appointment_time')
    return render(request, 'home.html', {'appointments': appointments})

def aboutus(request):
    return render (request,'aboutus.html',{})

def contactus(request):
    return render (request,'contactus.html',{})

def book_appointment(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        appointment_form = AppointmentForm(request.POST)

        if customer_form.is_valid() and appointment_form.is_valid():
            customer = customer_form.save()

            appointment = appointment_form.save(commit=False)
            appointment.customer = customer
            appointment.status = 'scheduled'
            appointment.save()

            messages.success(request, 'Your appointment has been booked successfully!')  
           # return redirect('home')  
    else:
        customer_form = CustomerForm()
        appointment_form = AppointmentForm()

    return render(request, 'book_appointment.html', {
        'customer_form': customer_form,
        'appointment_form': appointment_form
    })




# Create your views here.
