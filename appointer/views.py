from django.shortcuts             import render, redirect
from django.db.models             import Q
from rest_framework               import viewsets
from .forms                       import AppointmentForm
from .models                      import Appointment
from .serializers                 import AppointmentSerializer


def index(request):
    appointment = Appointment.objects.all()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return redirect('/')
    if request.is_ajax():
        q = request.GET.get("search")
        appointment = Appointment.objects.filter(Q(description__icontains=q) |
                                                 Q(time__icontains=q) |
                                                 Q(date__icontains=q))
        form = AppointmentForm()
        return render(request, "appointer/index.html",
                      {"appointment": appointment, "form": form})
    else:
        form = AppointmentForm()

    context = {"appointment": appointment, "form": form}
    return render(request, "appointer/index.html", context)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('date', 'time')
    serializer_class = AppointmentSerializer
