from django.urls import path
from.views import*

urlpatterns = [
    path('', hi, name="hello"),
    # path('api/register/', RegisterViews.as_view(), name="register"),
]


