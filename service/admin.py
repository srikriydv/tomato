from django.contrib import admin
from service.models import Login

class LoginAdmin(admin.ModelAdmin):
    list_display = ('image',)

# Register your models here.
admin.site.register(Login,LoginAdmin)