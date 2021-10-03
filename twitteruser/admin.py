from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import MyUser
 
class TwitterUserAdmin(UserAdmin):
   fieldsets = UserAdmin.fieldsets + (
       (None, {"fields": ("display_name",)}),
   )

admin.site.register(MyUser)

