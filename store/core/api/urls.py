from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.api.views import OrderModelViewSet

router = DefaultRouter()

router.register(r'orders', OrderModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
