from django.contrib import admin
from .models import Client,Tutor,Library,RequestDemo,BookClass,DemoCo
# Register your models here.
class client_admin(admin.ModelAdmin):
    list_display=('Name','Email','Standard','Phone')
    list_editable=('Email','Standard','Phone')
    search_fields=('Name','Standard')
    prepopulated_fields={'slug':('Name',)}
admin.site.register(Client,client_admin)


class tutor_admin(admin.ModelAdmin):
    list_display=('Name','Email','Qualification','Experience','Phone','Price','Subject')
    list_editable=('Email','Qualification','Experience','Phone')
    search_fields=('Name','Subject')
    prepopulated_fields={'slug':('Name',)}
admin.site.register(Tutor,tutor_admin)

class library_admin(admin.ModelAdmin):
    list_display=('Subject','Books')
    
    search_fields=('Subject','Books')
admin.site.register(Library,library_admin)

class requestdemo_admin(admin.ModelAdmin):
    list_display=('student','tutor','time','date','subject','standard')
admin.site.register(RequestDemo,requestdemo_admin)

class book_admin(admin.ModelAdmin):
    list_display=('student','tutor','time','date','subject','standard')
admin.site.register(BookClass,book_admin)

class demo_admin(admin.ModelAdmin):
    list_display=('student','tutor','time','date','subject','standard')
admin.site.register(DemoCo,demo_admin)
