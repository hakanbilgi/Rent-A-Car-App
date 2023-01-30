
from django.urls import path,include
from rest_framework import routers
from .views import CarView,ReservationView

router = routers.DefaultRouter()
router.register('car', CarView)
router.register('reservation', ReservationView)

urlpatterns = [
    path('', include(router.urls))
]