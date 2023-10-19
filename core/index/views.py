from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from accounts.models import User
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all().count()
        return context
    
class UserView(ListView):
    model = User
    paginate_by = 2