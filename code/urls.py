# appointments/urls.py
from django.urls import path
from .views import (
    AppointmentCreateView,
    PastAppointmentsListView,
    doctor_dashboard,
    update_appointment_status,
    delete_appointment,  # Only import existing views
)

app_name = 'appointments'

urlpatterns = [
    # Patient-facing URLs
    path('book/', 
         AppointmentCreateView.as_view(), 
         name='book_appointment'),
    path('my-appointments/', 
         PastAppointmentsListView.as_view(), 
         name='my_appointments'),
    path('past/', 
         PastAppointmentsListView.as_view(), 
         name='past_appointments'),

    # Doctor-facing URLs
    path('dashboard/', 
         doctor_dashboard, 
         name='dashboard'),
    path('appointments/accept/<int:appointment_id>/', 
         update_appointment_status, 
         {'new_status': 'accepted'}, 
         name='accept_appointment'),
    path('appointments/reject/<int:appointment_id>/', 
         update_appointment_status, 
         {'new_status': 'rejected'}, 
         name='reject_appointment'),
    path('appointments/delete/<int:appointment_id>/', 
         delete_appointment, 
         name='delete_appointment'),
]