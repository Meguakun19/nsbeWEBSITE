from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
# Create your views here.


def index(request):
    return HttpResponse("<h1>Just testing my program and learning about url mapping and views.</h1>")

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'