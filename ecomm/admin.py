from django.contrib import admin
from ecomm.models import SignUp

# Register your models here.
class SignUpadmin(admin.ModelAdmin):
    list_display=['username','email','phone','password','confirm_password']

admin.site.register(SignUp,SignUpadmin)
