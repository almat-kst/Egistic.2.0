from rest_framework import serializers

from .models import *
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'category']


class GenderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Gender
    fields = ['id', 'gender']


class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model = City
    fields = ['id','city']


class ScheduleTimeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ScheduleTime
    fields = ['id', 'schedule']


class TimeWorkSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeWork
    fields = ['id','time_work']


class HasExperienceSerializer(serializers.ModelSerializer):
  class Meta:
    model = HasExperience
    fields = ['has_experience']


class ExperienceYearSerializer(serializers.ModelSerializer):
  class Meta:
    model = ExperinceYear
    fields = ['experience_year']


class EducationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Education
    fields = ['education']


class LanguageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Language
    fields = ['language']


class SkillsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skills
    fields = ['skills']


class RemovalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Removal
    fields = ['removal']


class HasExperienceSerializer(serializers.ModelSerializer):
  class Meta:
    model = HasExperience
    fields = ['id', 'has_experience']

##################################################################################
class ListResumeSerializer(serializers.ModelSerializer): #list resume
  city = CitySerializer()
  schedule = ScheduleTimeSerializer()
  time_work = TimeWorkSerializer()
  category = CategorySerializer()

  class Meta:
    model = CreateResume
    fields = ['id','name', 'last_name', 'title', 'category', 'salary', 'get_image','city', 'schedule', 'time_work']


class DetailResumeSerializer(serializers.ModelSerializer): #for auth person detail resume
  gender = GenderSerializer()
  city = CitySerializer()
  has_experience = HasExperience()
  category = CategorySerializer()
  education = EducationSerializer()
  language = LanguageSerializer(many=True)
  skills = SkillsSerializer(many=True)
  travel = RemovalSerializer()
  schedule = ScheduleTimeSerializer()
  time_work = TimeWorkSerializer()

  class Meta:
    model = CreateResume
    fields = ['name', 'last_name', 'birth_date', 'gender', 'city', 'get_image',
    'has_experience', 'title', 'category', 'salary', 'education', 'language',
    'skills', 'last_place_work', 'data_finish', 'company_name',
    'status', 'info', 'travel', 'schedule', 'time_work', 'created']


class CreateResumeSerializer(serializers.ModelSerializer): #for creating resume
  # owner = serializers.ReadOnlyField()

  class Meta:
    model = CreateResume
    fields = ['name', 'last_name', 'birth_date', 'gender', 'city', 'get_image',
    'has_experience', 'title', 'category', 'salary', 'education', 'language',
    'skills', 'last_place_work', 'data_finish', 'company_name',
    'status', 'info', 'travel', 'schedule', 'time_work', 'created']
