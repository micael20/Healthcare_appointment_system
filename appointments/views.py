from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Doctor, Appointment, Patient

def index(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointments/index.html', {'doctors': doctors})

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    patient = Patient.objects.get(user=request.user)

    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        reason = request.POST['reason']
        Appointment.objects.create(
            doctor=doctor,
            patient=patient,
            date=date,
            time=time,
            reason=reason
        )
        return HttpResponseRedirect(reverse('appointments:index'))

    return render(request, 'appointments/book_appointment.html', {'doctor': doctor})

@login_required
def my_appointments(request):
    patient = Patient.objects.get(user=request.user)
    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'appointments/my_appointments.html', {'appointments': appointments})

# Create your views here.
