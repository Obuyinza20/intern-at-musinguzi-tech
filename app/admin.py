from django.contrib import admin
from .models import *

# Register your models here.

class InterneeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'second_name', 'institution' , 'course' , 'email' , 'phone_number']
    ordering =['id']


admin.site.register(Photo)
admin.site.register(Internee , InterneeAdmin)