from django.urls import path
from .views import *
from work import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='home'),
    path('work/', views.work, name='work'),
    path('plan/', views.plan, name='plan'),


]

urlpatterns += staticfiles_urlpatterns()
