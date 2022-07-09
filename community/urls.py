from django.urls import path

from community import views

urlpatterns = [
    path('', views.index),
    path('code/<int:code>', views.select_commu),
]
