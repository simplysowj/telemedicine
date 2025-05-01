from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.custom_login_view, name="login"),
     path("logout/", views.custom_logout_view, name="logout"),
     path("logged_out/", views.logged_out, name="logged_out"),
     path('video_call/<str:room_name>/', views.video_call, name='video_call'),
   # path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("dashboard/patient/", views.patient_dashboard, name="patient_dashboard"),
    path("dashboard/doctor/", views.doctor_dashboard, name="doctor_dashboard"),
]
