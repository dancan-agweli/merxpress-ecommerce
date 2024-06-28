from django.contrib import admin
from ecomm.models import SignUp,Order, OrderItem, Cancellation, Return, Refund, Product

# Register your models here.
class SignUpadmin(admin.ModelAdmin):
    list_display=['username','email','phone','password','confirm_password']

admin.site.register(SignUp,SignUpadmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cancellation)
admin.site.register(Return)
admin.site.register(Refund)
admin.site.register(Product)