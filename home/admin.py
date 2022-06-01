from django.contrib import admin
from home.models import Patient, Plogin
from home.models import Donor,Feedback
# Register your models here.

admin.site.register(Patient),
admin.site.register(Donor),
admin.site.register(Feedback),
