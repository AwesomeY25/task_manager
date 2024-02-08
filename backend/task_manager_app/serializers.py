from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_username', 'user_fname', 'user_lname', 'user_minitial', 'user_email', 'user_password', 'user_account_type', 'timestamp']