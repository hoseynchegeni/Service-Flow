from django.db.models.base import Model as Model
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task

# Create your views here.


class UserView(LoginRequiredMixin, ListView):
    model = User
    template_name = "registration/user_list.html"


class UserLogin(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse("index:home")


class UserLogout( LogoutView):
    def get_success_url(self):
        return reverse("accounts:login")


class CreateUser(LoginRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("index:home")


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ("first_name", "last_name", "image")
    template_name = "registration/update.html"
    success_url = reverse_lazy("accounts:users")


class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    template_name = "registration/detail.html"

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['user_permissions'] = user.user_permissions.all()
        context['user_created_task'] = Task.objects.filter(creator_id = user.id).count()
        return context


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "registration/delete.html"
    success_url = reverse_lazy("accounts:users")


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("index:home")
