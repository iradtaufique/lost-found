# from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from documents.models import Idcollection
from.Serializers import IdSerializer
from api.Serializers import *
# Create your views here.


class Listdata(ListAPIView):
    queryset = Idcollection.objects.all()
    serializer_class = IdSerializer


class Details(RetrieveAPIView):
    queryset = Idcollection.objects.all()
    serializer_class = IdSerializer


class Deletedataapi(DestroyAPIView):
    queryset = Idcollection.objects.all()
    serializer_class = IdSerializer


class Creatadataapi(CreateAPIView):
    queryset = Idcollection.objects.all()
    serializer_class = IdSerializer


User = get_user_model()


class CreateUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
