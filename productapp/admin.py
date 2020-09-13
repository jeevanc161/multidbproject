from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name', 'description' ,'sku' , 'price') 


admin.site.site_header = 'Admin Dashbord for Multi Database Project'
admin.site.register(Product , ProductAdmin)
