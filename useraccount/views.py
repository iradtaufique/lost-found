from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from documents.models import Idcollection
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import generics, status
from. serializers import RegisterSerializer
# Create your views here.

def hi(request):
    pass

