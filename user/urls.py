from django.urls import path
from user import views
app_name = "user"

urlpatterns = [
     path("register/", views.UserRegisterView.as_view(), name="register"),
     path("login/", views.UserLoginView.as_view(), name="login"),
]