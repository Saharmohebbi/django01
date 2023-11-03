from collections.abc import Iterable
from django.db import models
from accounts.models import UserProfile
from django.urls import reverse,reverse_lazy
from django.utils.text import slugify


class Post(models.Model):
    author=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=300,blank=True)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    like=models.ManyToManyField(UserProfile,related_name="post_like",blank=True)
    dislike=models.ManyToManyField(UserProfile,related_name="post_dislike",blank=True)
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
    
    def save(self,*args,**kwargs):
        super().save()
        if not self.slug:
            self.slug=slugify(self.title)
            self.save()
    
class Comment(models.Model):
    author=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.TextField()
    is_validate=models.BooleanField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.body}'
    

    
    
