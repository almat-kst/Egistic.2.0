"""egistic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

# from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('drf-auth/', include('rest_framework.urls')), # по сессиями
    path('auth/', include('djoser.urls')),         # по токенам
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('employer1/', include('employer.urls')),
    path('worker1/', include('worker1.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

###########################################################################
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns

# from worker.views import ResumeView
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'resume_just', ResumeView, basename='resume_just')

#     path('', include(router.urls)),

##########################################################################
# from rest_framework import routers
# from employer.views import *

# router = routers.DefaultRouter()
# router.register(r'', VakansiDetailView)

# path('employer/just/', include(router.urls)),
