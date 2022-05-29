from django.urls import path, include
from . import views

urlpatterns = [
  path('category_list/', views.CategoryView.as_view()),
  path('resume_list/', views.ListResumeView.as_view()),
  path('resume_detail/<int:pk>/', views.DetailResumeView.as_view()),
  path('create_resume/', views.CreateResumeView.as_view()),
  path('genders/', views.GenderView.as_view()),
  path('cities/', views.CityView.as_view()),
  path('schedule_times/', views.ScheduleTimeView.as_view()),
  path('time_works/', views.TimeWorkView.as_view()),
  path('has_experiences/', views.HasExperienceView.as_view()),
  path('experience_years/', views.ExperinceYearView.as_view()),
  path('educations/', views.EducationView.as_view()),
  path('languages/', views.LanguageView.as_view()),
  path('skills/', views.SkillsView.as_view()),
  path('removals/', views.RemovalView.as_view()),
  path('has_experience/', views.HasExperienceView.as_view()),
  # path('resume_filters/', views.FilterResumeView.as_view())
]