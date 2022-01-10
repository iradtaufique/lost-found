from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import*


class ID_list(admin.ModelAdmin):
    search_fields = ['first_name', 'idnumber',
                     'sector', 'district', 'second_name']

    def __str__(self):
        return self.idnumber
    list_display = ['first_name', 'second_name','birthdate', 'idnumber',
                     'sector', 'district','location',]


# Register your models here.
admin.site.register(Category,)
admin.site.register(Policepost,)
admin.site.register(Idcollection, ID_list)
# admin.site.register(Comment)
