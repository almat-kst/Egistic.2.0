from django.shortcuts import render

from .serializers import *
from .models import *
from .permissions import IsOwnerOrReadOnly
from .paginations import LeadPagination

from rest_framework import permissions
from rest_framework import generics

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class VakansiList(generics.ListAPIView):
  queryset = CreateVakansi.objects.all()
  serializer_class = ListVakansiSerializer
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('title',)
  search_fields = ('title',)
  pagination_class = LeadPagination


class CreateVakansiDetail(generics.CreateAPIView):
  queryset = CreateVakansi.objects.all()
  serializer_class = CreateVakansiSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VakansiDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = CreateVakansi.objects.all()
  serializer_class = DetailVakansiSerializer
  permission_classes = [IsOwnerOrReadOnly]


class CategoryView(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer


class TimeWorkView(generics.ListCreateAPIView):
  queryset = TimeWork.objects.all()
  serializer_class = TimeWorkSerializer


class ScheduleTimeView(generics.ListCreateAPIView):
  queryset = ScheduleTime.objects.all()
  serializer_class = ScheduleTimeSerializer


class RemovalView(generics.ListCreateAPIView):
  queryset = Removal.objects.all()
  serializer_class = RemovalSerializer


class CityView(generics.ListCreateAPIView):
  queryset = City.objects.all()
  serializer_class = CitySerializer