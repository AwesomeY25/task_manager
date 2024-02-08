from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class UserAdmin(admin.ModelAdmin):
  list_display=('user_id', 'user_username', 'user_fname', 'user_lname', 'user_minitial', 'user_email', 'user_password', 'user_account_type', 'timestamp')