from django.contrib import admin

from .models import Client
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name','schema_name',)


admin.site.register(Client, ClientAdmin)
