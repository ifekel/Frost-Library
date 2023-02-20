from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView

class DashboardPageView(LoginRequiredMixin, TemplateView):
    template_name = 'authenticated_user/dashboard.html'