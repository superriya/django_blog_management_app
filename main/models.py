from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .helpers import *
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='blog_images/')
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    excerpt = models.TextField(max_length=150)
    description = models.TextField(max_length=2000)
    category = models.CharField(max_length=200, default='Vega')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #tags
    tags = TaggableManager()
    
    def __str__(self):
        return self.title 
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title + " " + self.category + " ")
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    
    
    class Meta:
        ordering = (['-created_at'])
        verbose_name_plural = 'Comments'