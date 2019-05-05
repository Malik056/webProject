from django.urls import path
from . import views

app_name = 'Auth'
urlpatterns = [
    path('signup', views.Signup.as_view(), name="signup"),
    path('', views.LoginUser.as_view(), name="login"),
    path('homepage', views.homepage, name='homepage'),
    path('profile', views.getDetails, name='profile'),
    # path('login', views.login, name="login"),

    # API URLs
    # User Profile
    path('api/getmyprofile/<str:email>/<str:password>', views.GetProfileAPI.as_view()),
    path('api/updatemyprofile/<str:email>/<str:password>', views.UpdateProfileAPI.as_view()),
    path('api/createjob', views.CreateJobAPI.as_view()),
    path('api/readjobs', views.ReadJobsAPI.as_view()),
    path('api/updatejob/<int:pk>', views.UpdateJobAPI.as_view()),
    path('api/deletejob/<int:pk>', views.DeleteJobAPI.as_view()),
    path('api/createpost/<int:pk>', views.CreatePostAPI.as_view(), name="createPosts"),
    path('api/getallposts/<int:pk>', views.GetPostsAPI, name="getPosts")
]
