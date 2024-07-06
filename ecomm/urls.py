from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CancellationViewSet, ReturnViewSet, RefundViewSet, signup, login_view, logout_view, home

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'cancellations', CancellationViewSet)
router.register(r'returns', ReturnViewSet)
router.register(r'refunds', RefundViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/', include((router.urls, 'api'))),
]


