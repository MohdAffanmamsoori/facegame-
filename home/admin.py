# Bismillah Hir Rehman Nir Rahim


from home.models import Users
from django.contrib import admin
from home.models import Contactus, Userearns12,add_bank_details_user



# Register your models here.

admin.site.register(Contactus)

admin.site.register(Users)
admin.site.register(Userearns12)
admin.site.register(add_bank_details_user)

