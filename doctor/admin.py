from django.contrib import admin
from .models import Specialization, AvailableTime, Designation, Doctor, Review

# Register your models here.

class SpecializationModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
admin.site.register(Specialization, SpecializationModelAdmin)
    
admin.site.register(AvailableTime)

class DesignationModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
admin.site.register(Designation, DesignationModelAdmin)
    
admin.site.register(Doctor)

admin.site.register(Review)