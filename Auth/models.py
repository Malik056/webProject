from django.db import models
from datetime import datetime


# Create your models here.
class UserDetails(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    email = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=15)
    contactInfo = models.CharField(max_length=50, null=True)
    connections = models.ManyToManyField('self', null=True)

    def __str__(self):
        return self.firstName+" "+self.lastName


class LoggedinUsers(models.Model):
    userId = models.ForeignKey(UserDetails, on_delete=models.CASCADE)


class Posts(models.Model):
    postBy = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    postTitle = models.CharField(max_length=10000)
    postImage = models.CharField(max_length=1000)
    postDateTime = models.DateTimeField(auto_now_add=True)


class PostLikes(models.Model):
    postId = models.ForeignKey(Posts, on_delete=models.CASCADE)
    userId = models.ForeignKey(UserDetails, on_delete=models.CASCADE)


class PostComments(models.Model):
    postId = models.ForeignKey(Posts, on_delete=models.CASCADE)
    userId = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    commentText = models.CharField(max_length=2000)

    def __str__(self):
        return self.pk+". "+self.commentText


class JobsCategories(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Jobs(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)
    category = models.ForeignKey(JobsCategories, on_delete=models.CASCADE)
    posted_by = models.IntegerField()
    location = models.CharField(max_length=200)
    salary = models.IntegerField()
    experience = models.FloatField()

    def __str__(self):
        return self.title


class JobsApplications(models.Model):
    job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    applicant_id = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.jobid











