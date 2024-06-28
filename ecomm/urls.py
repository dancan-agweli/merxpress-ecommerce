from django.urls import path
from ecomm import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CancellationViewSet, ReturnViewSet, RefundViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'cancellations', CancellationViewSet)
router.register(r'returns', ReturnViewSet)
router.register(r'refunds', RefundViewSet)

urlpatterns=[
    path('',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('', include(router.urls))

]