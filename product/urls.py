from django.urls import path
from product import views

app_name = "product"
urlpatterns = [
    path("list/", views.ProductListView.as_view(), name="list"),
    path("create/", views.ProductCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", views.ProductDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", views.ProductUpdateView.as_view(), name="update"),
    path("cart/add/", views.AddToCartView.as_view(), name="add_to_cart"),
]
