from django.contrib import admin
from .models import Profile,Books,Comment,Review,Groups,Question
# Register your models here.
admin.site.register(Profile)
admin.site.register(Books)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(Groups)
admin.site.register(Question)