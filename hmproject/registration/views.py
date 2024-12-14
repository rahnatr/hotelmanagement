from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Hotel_Registration
from .serializers import CreateHotelDetailsSerializer 
# Create your views here.

# CREATE and LIST Hotels
class HotellistcreateView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Hotel_Registration.objects.all()
    serializer_class = CreateHotelDetailsSerializer
    
    #define get request
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    #define post request
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
# Retrieve and update Hotel
class HotelRetrieveUpdateView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Hotel_Registration.objects.all()
    serializer_class = CreateHotelDetailsSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) 
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs) #full update
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)  # Partial update 
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def head(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)  #same as the GET method but omits the content from the response body.
    
    def options(self, request, *args, **kwargs):
        return self.metadata_response() #returns the allowed HTTP methods.