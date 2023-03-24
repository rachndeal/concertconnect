from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    NAME_MAX_LENGTH = 128
    REVIEW_MAX_LENGTH = 500
    
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    venue_info = models.CharField(max_length = REVIEW_MAX_LENGTH, blank=True)
    likes = models.IntegerField(default=0)    
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200
    DES_MAX_LENGTH = 500
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=TITLE_MAX_LENGTH, unique = True)
    url = models.URLField()
    description = models.CharField (max_length = DES_MAX_LENGTH, blank=True)
    event_picture = models.CharField(max_length = URL_MAX_LENGTH, blank=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    
class UserProfile(models.Model):
    TEXT_MAX_LENGTH = 500
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    concerts = models.CharField(max_length=TEXT_MAX_LENGTH, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username

