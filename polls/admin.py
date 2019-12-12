from django.contrib import admin
from .models import Patient, Medicine, Provided_Medicine


admin.site.register(Patient)
admin.site.register(Medicine)
admin.site.register(Provided_Medicine)



