from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import HotellistcreateView, HotelRetrieveUpdateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hotels/',HotellistcreateView.as_view(),name='hotel-list-create'),
     path('hotels/<int:pk>/',HotelRetrieveUpdateView.as_view(),name='hotel-retrieve-update'),
]

