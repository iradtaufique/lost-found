from django.urls import path, include
from .views import*


urlpatterns = [
    path('', Listdata.as_view(), name="listdataapi"),
    path('details/<int:pk>/', Details.as_view(), name="apidetails"),
    path('create/', Creatadataapi.as_view(), name="apicreate"),
    path('delete/<int:pk>/', Deletedataapi.as_view(), name="apicreate"),
    path('registeruser/', CreateUserAPIView.as_view(), name="registeruser"),
    # path('auth/', include('rest_auth.urls')),
]
