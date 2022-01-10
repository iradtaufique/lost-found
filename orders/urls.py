from django.urls import path
from .views import*
urlpatterns = [
    path('', CreateOrder.as_view(), name="ordering"),
     path('contact/', contactus, name="contact_us"),
]
