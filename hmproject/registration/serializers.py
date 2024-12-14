
from rest_framework.serializers import ModelSerializer
from .models import Hotel_Registration

class CreateHotelDetailsSerializer(ModelSerializer):
    class Meta:
        model = Hotel_Registration
        fields = '__all__' 
        
