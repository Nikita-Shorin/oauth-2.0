from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from allauth.socialaccount.models import SocialAccount


class IndexView(TemplateView):
    template_name = "main/index.html"


class AuthenticatedView(LoginRequiredMixin, TemplateView):
    template_name = "main/authenticated.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        soc_user = SocialAccount.objects.filter(user=user).first()
        print(soc_user)
        context["soc_user"] = soc_user
        context["user"] = user

        return context


class MyLogoutView(LogoutView):
    login_url = "/login"

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        return redirect(reverse_lazy("index"))
