from django.db import models
from django.contrib.auth.models import User


# # Create your models here.
# class User (AbstractBaseUser):
#     """
#     Custom user class.
#     """
#     email = models.EmailField('email address', unique=True, db_index=True)
#     joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'

#     def __str__(self):
#         return self.email


class Todo (models.Model):
    user = models.ForeignKey(User, null=False)
    todo_text = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return ("done: " + str(self.done) + ", archived: "
                + str(self.archived) + ", text: " + self.todo_text)
