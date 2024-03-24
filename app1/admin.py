from django.contrib import admin
from app1.models import employee



class employeede(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eadd']

# Register your models here.
admin.site.register(employee,employeede)

