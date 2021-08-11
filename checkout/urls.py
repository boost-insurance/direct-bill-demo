from django.urls import path

from checkout.views import CheckoutView, index_view

urlpatterns = [path("", index_view), path("checkout", CheckoutView.as_view())]
