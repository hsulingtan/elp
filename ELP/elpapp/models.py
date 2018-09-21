from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EUserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='proile_pics',blank=True)
    def __str__(self):
        return self.user.username

class SUserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='proile_pics',blank=True)
    def __str__(self):
        return self.user.username

#class UserProfileInfo(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    portfolio_site = models.URLField(blank=True)
#    profile_pic = models.ImageField(upload_to='proile_pics',blank=True)
#    def __str__(self):
#        return self.user.username

class Employer(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    email = models.EmailField(max_length=264,unique=True,default='something@somemail.com')


class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264,unique=True,default='something@somemail.com')



class jobs(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=264)
    job_desc = models.CharField(max_length=264)


class AccessRecord(models.Model):
    title = models.ForeignKey(jobs, on_delete=models.CASCADE)
    date = models.DateField()
