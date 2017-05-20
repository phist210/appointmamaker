from django.http                  import Http404
from django.shortcuts             import render, redirect
from rest_framework               import viewsets
from .forms                       import AppointmentForm
from .models                      import Appointment
from .serializers                 import AppointmentSerializer


def index(request):
    try:
        appointment = Appointment.objects.all()
    except Appointment.DoesNotExist:
        raise Http404("Appointment does not exist")
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return redirect('/', pk=appointment.pk)
    else:
        form = AppointmentForm()

    context = {"appointment": appointment, "form": form}
    return render(request, "appointer/index.html", context)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('date', 'time')
    serializer_class = AppointmentSerializer
