from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('registration', views.regist),
    path('test', views.test),
]
