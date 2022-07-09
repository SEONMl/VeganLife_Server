from django.urls import path

from member import views

urlpatterns = [
    path('', views.member_api),
    path('email/<str:email>/', views.member_with_email),
]