"""All urls for the direct_bill_demo service."""
from django.urls import include, path

urlpatterns = [path("", include("checkout.urls"))]
