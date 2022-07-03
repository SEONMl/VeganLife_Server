from django.urls import path

from member import views

urlpatterns = [
    path('signup/', views.sign_up),
    path('signin/', views.sign_in),
    path('', views.member_api),
]