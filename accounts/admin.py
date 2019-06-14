from django.contrib import admin
from .models import UserProfile, EmployeeProfile, ClientProfile

class UserProfileAdmin(admin.ModelAdmin): 
    list_display = ( 'user', 'get_name', 'dob', 'rank', 'user_status', 'active')
    search_fields = ['user', 'gender', 'phone_number']
    list_filter = ['rank', 'active', 'reg_date', 'gender']

    class Meta:
    	model = UserProfile

class EmployeeAdmin(admin.ModelAdmin): 
    list_display = ( 'profile', 'active')
    search_fields = ['profile', ]
    # list_filter = ['rank', 'active', 'reg_date', 'gender']
    class Meta:
    	model = EmployeeProfile

class ClientAdmin(admin.ModelAdmin): 
    list_display = ( 'profile', 'active')
    search_fields = ['profile', ]

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmployeeProfile, EmployeeAdmin)
admin.site.register(ClientProfile, ClientAdmin)