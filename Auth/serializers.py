from rest_framework import serializers
from .models import UserDetails, Jobs, JobsCategories, Posts, PostComments, PostLikes


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserDetails
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jobs
        fields = '__all__'


class PostSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = '__all__'

