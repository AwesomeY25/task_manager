from django.db import models

class User(models.Model):
    
    class AccountType(models.TextChoices):
        INTERN = 'I', 'Intern'
        DEPT_SUPERVISOR = 'DS', 'Department Supervisor'
        
    user_id = models.IntegerField()
    user_username = models.CharField(max_length = 255)
    user_fname = models.CharField(max_length = 255)
    user_lname = models.CharField(max_length = 255)
    user_minitial = models.CharField(max_length = 255)
    user_email = models.CharField(max_length = 255)
    user_password = models.CharField(max_length = 255)
    user_account_type = models.CharField(
        max_length=2,
        choices=AccountType.choices,
        default=AccountType.INTERN)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    def __str__(self):
        return self.user_id
    
# Task