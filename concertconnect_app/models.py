from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Don't forget to migrate any new models "python manage.py makemigrations concertconnect" "python manage.py migrate"
# NEED TO CREATE SUPERUSER

class UserProfile(models.Models):
	#Links UserProfile to User model instance
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	picture = models.ImageField(upload_to(''), blank = True)
	is_owner = models.BooleanField()
#if lacking time, could remove the Owner option and make all users same type

	def __str__(self):
		return self.user.username


class Concert(models.Models):

	name = models.CharField(max_length= 128, unique=True)
	description = models.CharField (max_length = 500)
	venue = models.CharField(max_length = 64)
	address = models.CharField(max_length = 100)
	name_slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):
		self.name_slug = slugify(self.name)
		super(Venue, self).save(*args, **kwargs)

	def __str__(self):
		return self.name
#attribute each Concert to a Venue Owner


class Review(models.Models):

	review = models.CharField(max_length = 500, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	#should have an 'about' foreignkey but on Venue or Concert or another User??

	def __str__(self):
		return "Review written by" + self.author.user.username

# Potentially: class Venue(model.Models):

