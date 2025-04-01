from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Admin_Helath_CSV)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Feedback)
admin.site.register(Search_Data)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'scheduled_time', 'status')
    list_filter = ('status', 'scheduled_time')
    search_fields = ('patient__username', 'doctor__name')
