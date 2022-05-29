from .models import *
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = ['id', 'name', 'info', 'vakansi', 'address', 'number']


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'category']


class ScheduleTimeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ScheduleTime
    fields = ['id', 'schedule']


class TimeWorkSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeWork
    fields = ['id','time_work']


class RemovalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Removal
    fields = ['id', 'removal']


class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = ['id', 'city']


class ListVakansiSerializer(serializers.ModelSerializer):
  category = CategorySerializer()
  travel = RemovalSerializer()
  schedule = ScheduleTimeSerializer()
  time_work = TimeWorkSerializer()
  city = CitySerializer()

  class Meta:
    model = CreateVakansi
    fields = ['id', 'title', 'category','city', 'company_name', 'salary_start', 'salary_end', 'travel', 'schedule', 'time_work']


class DetailVakansiSerializer(serializers.ModelSerializer):
  category = CategorySerializer()
  travel = RemovalSerializer()
  schedule = ScheduleTimeSerializer()
  time_work = TimeWorkSerializer()
  city = CitySerializer()
  
  class Meta:
    model = CreateVakansi
    fields = ['id', 'title', 'category', 'company_name', 'city', 'salary_start', 'salary_end', 'travel', 'schedule', 'time_work', 'obligations', 'requirements', 'conditions']


class CreateVakansiSerializer(serializers.ModelSerializer):
  class Meta:
    model = CreateVakansi
    fields = ['id', 'title', 'category', 'salary_start', 'salary_end', 'travel', 'schedule', 'time_work', 'obligations', 'requirements', 'conditions']