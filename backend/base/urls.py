from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_routes, name="routes"),
    path("real_estates/", views.get_real_estates, name="real_estates"),
    path("real_estate/<str:pk>", views.get_real_estate, name="real_estate"),
]
