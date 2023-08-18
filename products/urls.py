from django.urls import path
from . import views

urlpatterns = [
    # specifies the root of this app
    path("", views.index),
    path("new/", views.new)
]

