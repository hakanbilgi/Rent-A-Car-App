from rest_framework.viewsets import ModelViewSet
from .models import Car,Reservation
from .serializer import CarSerializer,ReservationSerializer
# from .permissions import IsStafforReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]
    
    
class ReservationView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]