from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.conf import settings

from user.forms import UserLoginForm, UserRegistrationForm

class UserRegisterView(views.CreateView):
    template_name = "registration/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("master:home")

    def form_valid(self, form):
        data = form.cleaned_data
        email = data["email"]
        form.instance.username = email
        return super().form_valid(form)

class UserLoginView(auth_views.LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True

class UserLoginView(views.View):
    template_name = "registration/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("master:dashboard")

    def get(self, request):
        context = {"form": self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request):

        form = self.form_class(request.POST)
        
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def get_success_url(self):
        redirect_url = settings.LOGIN_REDIRECT_URL
        if self.success_url is None:
            return redirect_url
        return self.success_url

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)
        username = data.get("username")
        password = data.get("password")

        user = auth.authenticate(self.request, username=username, password=password)
        if user is not None:
            auth.login(self.request, user)
            return redirect(self.get_success_url())
        return self.form_invalid(form)

    def form_invalid(self, form):
        context = {"form": form}
        return render(self.request, self.template_name, context)
