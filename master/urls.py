from django.urls import path
from master import views

app_name = "master"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/",views.about_view, name="about"),
    path("contact/",views.contact_view, name="contact"),
    path("login/", views.login_view, name="login"),
    # path("dashboard/", views.DashboardView.as_view(), name="dashboard"),



]