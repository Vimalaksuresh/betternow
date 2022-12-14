
from django.conf import settings
from django.shortcuts import render
from django.views import generic as views
from django.urls import reverse_lazy
from user.forms import UserRegistrationForm
from django.conf import settings
from customer.models import Customer
from product.models import ProductModel
from user.models import Profile
from django.http import HttpResponse
from django.core.mail import send_mail
from master.forms import FeedbackForm

from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin






def home_view(request):
    template_name = 'master/home.html'
    return render(request, template_name)

def about_view(request):
    template_name = "master/about.html"
    return render(request, template_name)

def contact_view(request):
    template_name = "master/contact.html"
    return render(request, template_name)

def login_view(request):
    template_name = "master/login.html"
    return render(request, template_name)




# class based view
class HomeView(views.TemplateView):
    template_name = 'master/home.html'
    extra_context = {"form": UserRegistrationForm}


class DashboardView(views.View):
    template_name = "user/dashboard.html"

    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request):
        pass

    # def get_context_data(self) -> dict:
    #     user = self.request.user
    #     customer = Customer.objects.get(user=user)
    #     products = ProductModel.objects.filter(enroll__customer=customer)
    #     profile = Profile.objects.filter(customer=customer).first()
    #     context = {"products": products, "profile": profile}
    #     return context


class FeedbackView(views.FormView):
    template_name = "master/feedback.html"
    form_class = FeedbackForm
    success_url = reverse_lazy("master:home")

    def from_valid(self, form):
        data = form.cleaned_data
        subject = "Thankyou for your valuable feedback!"
        message = f"""
        Hi {data.get("name")},
        
        This is an auto generated mail.we will reach you soon.
        
        Thanks and Regards,
        Learning Team
        """
        from_mail = settings.EMAIL_HOST_USER
        to_mail =[
            data.get("email"),
        ]
        send_mail(subject=subject, message=message, from_mail=from_mail, recipient_list=to_mail)
        return super().form_valid(form)
