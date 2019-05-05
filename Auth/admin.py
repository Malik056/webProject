from django.contrib import admin
from .models import UserDetails, Jobs, Posts, PostComments, PostLikes, JobsCategories

admin.site.register(UserDetails)
admin.site.register(Jobs)
admin.site.register(Posts)
admin.site.register(PostLikes)
admin.site.register(PostComments)
admin.site.register(JobsCategories)



# Register your models here.
