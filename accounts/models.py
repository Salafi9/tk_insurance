from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


# Create your models here.
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

RANK = (
    ('Admin', 'Admin'),
    ('Employee', 'Employee'),
    ('Client', 'Client')
)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='profile')
    uid = models.UUIDField(default=uuid4, editable=False)
    image = models.ImageField(blank=True, null=True, upload_to='profile_pics')
    address = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    gender = models.CharField(default="Others", blank=True, null=True, max_length=6, help_text="Gender", choices=GENDER)
    dob = models.DateField(blank=True, null=True,help_text='Date of Birth')
    reg_date = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    rank = models.CharField(default='Client', max_length=15, help_text="Rank", choices=RANK)
    active = models.BooleanField(default=False)

    class Meta: 
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        ordering = ["-reg_date", 'user']

    def get_name(self):
        if self.user.first_name and self.user.last_name:
            return str(self.user.first_name) + " " + str(self.user.last_name) 
        else:
            return str(self.user.username)

    def user_status(self):
        if self.rank == "Admin":
            return "Admin"
        elif self.rank == "Employee":
            return "Employee"
        elif self.rank == "Client":
            return "Client"
        else:
            return "User Status Not Defined"

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return str(self.user.first_name) + " " + str(self.user.last_name) 
        else:
            return str(self.user.username)

class EmployeeProfile(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE,  related_name='employee_profile')
    uid = models.UUIDField(default=uuid4, editable=True)
    about = models.TextField(blank=True, null=True)
    fb_link = models.URLField(blank=True, null=True)
    tw_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    active = models.BooleanField(default=False)
  
    def __str__(self):
    	return str(self.profile)

    class Meta: 
        verbose_name = 'Employee Profile'
        verbose_name_plural = 'Employees Profiles'
        ordering = ["-reg_date", 'profile']


class ClientProfile(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE,  related_name='client_profile')
    uid = models.UUIDField(default=uuid4, editable=True)
    about = models.TextField(blank=True, null=True)
    fb_link = models.URLField(blank=True, null=True)
    tw_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    active = models.BooleanField(default=True)
  
    def __str__(self):
    	return str(self.profile)

    class Meta: 
        verbose_name = 'Client Profile'
        verbose_name_plural = 'Clients Profiles'
        ordering = ["-reg_date", 'profile']