from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate,login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Auth.models import UserDetails,LoggedinUsers
from django.http import HttpResponse

# Create your views here.

class GetAllPost(View):
    template_name=""



