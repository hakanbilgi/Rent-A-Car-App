from rest_framework import serializers
from .models import Car,Reservation

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'plate_number',
            'brand',
            'model',
            'year',
            'gear',
            'rent_per_day',
            'availability'
        )
        
        
class ReservationSerializer(serializers.ModelSerializer):
    
    car = serializers.StringRelatedField()
    car_id = serializers.IntegerField()
    customer = serializers.StringRelatedField()
    customer_id = serializers.IntegerField()
    
    class Meta:
        model = Reservation
        fields = (
            'id',
            'start_date',
            'end_date',
            'car',
            'car_id',
            'customer',
            'customer_id'
        )
        
