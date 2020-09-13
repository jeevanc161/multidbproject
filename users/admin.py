from django.contrib import admin
from .models import DatabaseList , Userdb
# Register your models here.

class UserdbAdmin(admin.ModelAdmin): 
    list_display = ('user', 'get_assign_db') 


admin.site.site_header = 'Admin Dashbord for Multi Database Project'
admin.site.register(DatabaseList)
admin.site.register(Userdb , UserdbAdmin)
