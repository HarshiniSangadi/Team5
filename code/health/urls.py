from django.urls import path
from .views import AppointmentCreateView, PastAppointmentsListView, doctor_dashboard, update_appointment_status

app_name = 'appointments'

urlpatterns = [
    path('book/', AppointmentCreateView.as_view(), name='book_appointment'),
    # Add the following line:
    path('my-appointments/', PastAppointmentsListView.as_view(), name='my_appointments'),
    path('past/', PastAppointmentsListView.as_view(), name='past_appointments'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('doctor/update/<int:appointment_id>/<str:new_status>/', update_appointment_status, name='update_status'),
]