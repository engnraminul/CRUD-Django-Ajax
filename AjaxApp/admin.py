from django.contrib import admin
from .models import Crud

class CustomAdmin(admin.ModelAdmin):
    list_filter = ('city',)
    list_display = ('name', 'phone', 'city',)


admin.site.register(Crud, CustomAdmin)


