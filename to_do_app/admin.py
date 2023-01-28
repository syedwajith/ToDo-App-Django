from django.contrib import admin
from to_do_app.models import ToDo_Datas

# Register your models here.

class ToDo_Admin(admin.ModelAdmin):
    cols = ['Content','Date']
    
admin.site.register(ToDo_Datas,ToDo_Admin)