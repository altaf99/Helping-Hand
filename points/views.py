from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
# from django.contrib.auth import login, logout
from django.views.generic import CreateView, TemplateView
# from . import forms

class PointView(TemplateView):
    template_name = 'point.html'
