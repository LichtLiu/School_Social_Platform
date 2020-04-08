from django.db import models
from user.models import User

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateField(auto_now=True)
    pub_date = models.DateField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment
    


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateField(auto_now=True)
    pub_date = models.DateField(auto_now_add=True)
    content = models.TextField()
    comment = models.ManyToManyField(Comment, blank=True)

    class Meta:
        ordering = ['-pub_date']
        def __str__(self):
            return self.title
        
