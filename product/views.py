from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth import get_user_model
from product.forms import ProductForm
from product.models import Cart, CartItem, ProductModel


USER = get_user_model()

# formview
class ProductCreateView(views.CreateView):
    template_name = "product/form.html"
    model = ProductModel
    form_class = ProductForm
    success_url = reverse_lazy("product:list")
    extra_context = {"action": "create"}

    # def from_valid(self, form):
    #     form.instance.user = self.request.user
    #     form.save()
    #     return super().form_valid(form)
    def get(self, request):
        context = {"form": self.form_class()}
        context.update(self.extra_context)
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        context = {"form": form}
        context.update(self.extra_context)
        return render(self.request, self.template_name, context)


class ProductListView(views.ListView):
    template_name = "product/list.html"
    model = ProductModel
    context_object_name = "product"

    def get_queryset(self):
        qs = ProductModel.objects.filter(status=True)
        return qs


# detail view
class ProductDetailView(views.DetailView):
    template_name = "product/detail.html"
    model = ProductModel
    context_object_name = "product"

    def get_queryset(self):
        qs = ProductModel.objects.filter(status=True)
        return qs


# product update
class ProductUpdateView(views.UpdateView):
    template_name = "product/form.html"
    model = ProductModel
    form_class = ProductForm
    success_url = reverse_lazy("product:list")
    extra_context = {"action": "update"}

    # def get_queryset(self):
    #     qs = ProductModel.objects.filter(status=True)
    #     return qs


# delete course
class ProductDeleteView(views.DeleteView):
    template_name = "product/form.html"
    model = ProductModel
    success_url = reverse_lazy("product:list")
    extra_context = {"action": "Delete", "info": "Are you sure want to delete"}

    def form_valid(self, form):
        self.object.status = False
        self.object.save()
        url = super().get_success_url()
        return redirect(url)


class AddToCartView(LoginRequiredMixin, views.View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        user = request.user

        product = product.objects.filter(id=product_id).first()
        cart, created = Cart.objects.get_or_create(user=user, status=True)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity

        messages.success(request, "Added successfully!")
        return redirect(reverse_lazy("product:list"))
