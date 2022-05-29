from django.urls import path, include
from . import views

urlpatterns = [
  path('vakansi_list/', views.VakansiList.as_view()),
  path('vakansi_detail/<int:pk>/', views.VakansiDetail.as_view()),
  path('create_vakansi/', views.CreateVakansiDetail.as_view()),
  path('category/', views.CategoryView.as_view()),
  path('schedule_time/', views.ScheduleTimeView.as_view()),
  path('time_work', views.TimeWorkView.as_view()),
  path('travel/', views.RemovalView.as_view()),
  path('city/', views.CityView.as_view()),
]
