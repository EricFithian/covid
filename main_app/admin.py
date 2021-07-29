from django.contrib import admin
from .models import Patient, Test, Vaccine, Vaccinating, Testing

# Register your models here.

admin.site.register(Patient)
admin.site.register(Test)
admin.site.register(Vaccine)
admin.site.register(Vaccinating)
admin.site.register(Testing)
