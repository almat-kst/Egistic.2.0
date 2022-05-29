from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from rest_framework import permissions
from rest_framework import status

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from .paginations import LeadPagination


class CategoryView(APIView):
  def get(self, request, format=None):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


class ListResumeView(generics.ListAPIView):
  queryset = CreateResume.objects.all()
  serializer_class = ListResumeSerializer
  pagination_class = LeadPagination
  filter_backends = (DjangoFilterBackend, SearchFilter)
  filter_fields = ('title', 'city', 'category', 'schedule', 'time_work', 'salary')
  search_fields = ['title', 'city__city','category__category', 'schedule__schedule', 'time_work__time_work'] #'title', 'city', 'schedule', 'time_work'


class DetailResumeView(generics.RetrieveUpdateDestroyAPIView):
  queryset = CreateResume.objects.all()
  serializer_class = DetailResumeSerializer
  permission_classes = [IsOwnerOrReadOnly]


class CreateResumeView(generics.CreateAPIView):
  queryset = CreateResume.objects.all()
  serializer_class = CreateResumeSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GenderView(generics.ListAPIView):
  queryset = Gender.objects.all()
  serializer_class = GenderSerializer


class CityView(generics.ListAPIView):
  queryset = City.objects.all()
  serializer_class = CitySerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = ('id',)


class ScheduleTimeView(generics.ListAPIView):
  queryset = ScheduleTime.objects.all()
  serializer_class = ScheduleTimeSerializer
  filter_backends = (DjangoFilterBackend, )
  filter_fields = ('schedule', )


class TimeWorkView(generics.ListAPIView):
  queryset = TimeWork.objects.all()
  serializer_class = TimeWorkSerializer
  filter_backends = (DjangoFilterBackend, )
  filter_fields = ('id', )


class HasExperienceView(generics.ListAPIView):
  queryset = HasExperience.objects.all()
  serializer_class = HasExperienceSerializer


class ExperinceYearView(generics.ListAPIView):
  queryset = ExperinceYear.objects.all()
  serializer_class = ExperienceYearSerializer


class EducationView(generics.ListAPIView):
  queryset = Education.objects.all()
  serializer_class = EducationSerializer


class LanguageView(generics.ListAPIView):
  queryset = Language.objects.all()
  serializer_class = LanguageSerializer


class SkillsView(generics.ListAPIView):
  queryset = Skills.objects.all()
  serializer_class = SkillsSerializer


class RemovalView(generics.ListAPIView):
  queryset = Removal.objects.all()
  serializer_class = RemovalSerializer


class HasExperienceView(generics.ListAPIView):
  queryset = HasExperience.objects.all()
  serializer_class = HasExperienceSerializer

# class FilterResumeView(generics.ListAPIView):
#   queryset = CreateResume.objects.all()
#   serializer_class = FilterResumeSerializer
# class DetailResumeView(APIView):
#   permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#   def get_object(self, category_id, product_id):
#     try:
#         return CreateResume.objects.filter(category__id=category_id).get(id=product_id)
#     except CreateResume.DoesNotExist:
#         raise Http404

#   def get(self, request, category_id, product_id, format=None):
#     resume = self.get_object(category_id, product_id)
#     serializer = DetailResumeSerializer(resume)
#     return Response(serializer.data)

#   def get_object(self, category_id, product_id):
#     try:
#         return CreateResume.objects.filter(category__id=category_id).get(id=product_id)
#     except CreateResume.DoesNotExist:
#         raise Http404

#   def get(self, request, category_id, product_id, format=None):
#     resume = self.get_object(category_id, product_id)
#     serializer = DetailResumeSerializer(resume)
#     return Response(serializer.data)

#   def put(self, request, category_id, product_id, format=None):
#     resume = self.get_object(category_id, product_id)
#     serializer = DetailResumeSerializer(resume, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#   def post(self, request, format=None):
#     serializer = DetailResumeSerializer(data = request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#   def delete(self, request, category_id, product_id, format=None):
#     resume = self.get_object(category_id, product_id)
#     resume.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)