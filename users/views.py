from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from users.models import User

# Create your views here.

class UserList(ListView):
    model = User

class UserView(DetailView):
    model = User

class UserCreate(CreateView):
    model = User
    fields = ['name', 'email']
    success_url = reverse_lazy('user_list')

class UserUpdate(UpdateView):
    model = User
    fields = ['name', 'email']
    status = reverse_lazy('user_list')

class UserDelete(DeleteView):
    model = User
    status = reverse_lazy('user_list')