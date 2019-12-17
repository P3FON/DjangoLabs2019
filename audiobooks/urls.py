from django.urls import path

from audiobooks import views

urlpatterns = [
    path('', views.index, name='index')
]