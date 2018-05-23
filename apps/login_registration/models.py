from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "Login should not be empty"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Login should not be empty"
        if len(postData['email']) < 2:
            errors["email"] = "Login should not be empty"
        
        if len(postData['login']) < 4:
            errors["login"] = "Login should be more than 4 characters"
        if len(postData['password']) < 2:
            errors["password"] = "Password should not be empty"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be more than 8 characters"
        return errors
class Users(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True , null=True)
    def __repr__(self):
        return "<users object: {} {}>".format(self.first_name, self.last_name)
    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    objects = UsersManager()