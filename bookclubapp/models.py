from django.db import models

class Book:
    def __init__(self, id,title, author, description, pagecount, average_rating, image_Links):
        self.id=id
        self.title=title
        self.author=author
        self.pagecount=pagecount
        self.image_Links=image_Links
        self.description=description
        self.average_rating=average_rating


