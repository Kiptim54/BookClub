from django.db import models
from django.contrib.auth.models import User



class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.TextField()
    time_posted=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-time_posted']

    def __str__(self):
        return self.user


class Review(models.Model):
    title=models.CharField(max_length=250)
    Review=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    comments=models.ForeignKey(Comment, on_delete=models.CASCADE)
    time_posted=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-time_posted']

    def __str__(self):
        return self.title
        
class Books(models.Model):
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    reviews=models.ForeignKey(Review, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    Email=models.EmailField()
    reviews=models.ForeignKey(Review,on_delete=models.CASCADE, null=True)
    comments=models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    books=models.ManyToManyField(Books, null=True)

    def __str__(self):
        return self.name

class Groups(models.Model):
    Group_name=models.CharField(max_length=250)
    members=models.ManyToManyField(Profile, null=True)
    books=models.ManyToManyField(Books, null=True)

    def __str__(self):
        return self.Group_name

class Book:
    def __init__(self, id,title, author, description, pagecount, average_rating, image_Links):
        self.id=id
        self.title=title
        self.author=author
        self.pagecount=pagecount
        self.image_Links=image_Links
        self.description=description
        self.average_rating=average_rating




