from django.urls import path

from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("authenticated/", AuthenticatedView.as_view(), name="authenticated"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
]
