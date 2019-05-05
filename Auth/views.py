from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate,login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UserDetails,LoggedinUsers
from django.http import HttpResponse, Http404

from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from django.http import JsonResponse
from .serializers import *
# Create your views here.


def homepage(request):
    return render(request, 'Auth/homepage.html')


def login(request):
    return render(request, 'Auth/Index.html', {"session": "session"})


def loginuser(request):

    return render(request, 'Auth/Index.html')
    #
    # try:
    #     user = UserDetails.objects.get(email="email@email.com")
    #     if user.password == "pass1234":
    #         loguser = LoggedinUsers(userId=user.pk)
    #         loguser.save()
    #         return render(request, 'Auth/Signup.html', {'User', user})
    #     else:
    #         return render(request, 'Auth/Index.html', {'error': "*Invalid credentials"})
    #
    # except UserDetails.DoesNotExist:
    #     return render(request, 'Auth/Index.html', {'error': "*Invalid credentials"})


def getDetails(request):
    user = UserDetails.objects.get(pk=8)
    return render(request, 'Auth/profile.html', {"user": user})


class LoginUser(View):
    def get(self, request):
        return render(request, 'Auth/Index.html')

    def post(self, request):
        em = request.POST['email']
        pa = request.POST['pswd']
        try:
            userDetails = UserDetails.objects.get(email=em)
        except UserDetails.DoesNotExist:
            return render(request, "Auth/Index.html", {"error": "Invalid Credentials"})
        else:
            if userDetails.password == pa:
                return render(request, "Auth/homepage.html", {"user": userDetails})
            else:
                return render(request, "Auth/Index.html", {"error": "Invalid password"})

        return redirect('Auth:homepage')


class Signup(View):

    def get(self, request):
        return render(request, 'Auth/Signup.html')

    def post(self, request):
        fn = request.POST['Firstname']
        ln = request.POST['Lastname']
        em = request.POST['stuEmail']
        pa = request.POST['stuPassword']
        cn = request.POST['stuContact']
        from django.core.mail import send_mail

        send_mail('Subject here', 'Here is the message.', 'from@example.com',
                  ['tahamahmoodmalik@gmail.com'], fail_silently=False)
        try:
            userDetails = UserDetails.objects.get(email=em)
        except UserDetails.DoesNotExist:
            newUser = UserDetails(firstName=fn, lastName=ln, email=em, contactInfo=cn, password=pa)
            newUser.save()
            return render(request, "Auth/homepage.html", {"user": newUser})

        else:
            return render(request, "Auth/Signup.html", {"error": "User with this email already exists"})


# API view
class GetProfileAPI(RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'email'

    def get_queryset(self):
        user = UserDetails.objects.filter(email=self.kwargs['email'])
        print(user[0].email)
        # return user
        if user[0].password == self.kwargs['password']:
            return user
        else:
            return UserDetails.objects.filter(email='notFound@notFound.FoundNot')


class UpdateProfileAPI(UpdateAPIView):
    serializer_class = UserSerializer
    # queryset = UserDetails.objects.all()
    lookup_field = 'email'

    def get_queryset(self):
        user = UserDetails.objects.filter(email=self.kwargs['email'])
        if user.exists():

            print(user[0].email)
            # return user
            if user[0].password == self.kwargs['password']:
                return user
            else:
                return UserDetails.objects.filter(email='notFound@notFound.FoundNot')


class SearchUserAPI(ListCreateAPIView):
    serializer_class = UserSerializer


class CreateJobAPI(CreateAPIView):
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()


class ReadJobsAPI(ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        return Jobs.objects.all()


class UpdateJobAPI(UpdateAPIView):
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()


class DeleteJobAPI(DestroyAPIView):
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()


class CreatePostAPI(CreateAPIView):
    serializer_class = PostSerilizer
    queryset = Posts.objects.filter()


class GetPostsAPI(ListAPIView):
    serializer_class = PostSerilizer
    queryset = Posts.objects.all()


