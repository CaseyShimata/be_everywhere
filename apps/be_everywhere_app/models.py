from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def regvalidation(self, postData):
        errors = []
        if len(postData['first']) < 2:
            errors.append("First name must be at least 2 character.")
        if (postData['first'].replace(' ','').isalpha() == False):
            errors.append("First name must only be letters.")
        if len(postData['last']) < 2:
            errors.append("Last name must be at least 2 character.")
        if (postData['last'].replace(' ','').isalpha() == False):
            errors.append("Last name must only be letters.")
        if not EMAIL_REGEX.match(postData['email']):
            errors.append("Not a valid email.")
        if Users.objects.filter(email=postData['email']):
            errors.append("Email already taken.")
        if len(postData['password']) < 8:
            errors.append("Password must be at least 8 characters.")
        elif postData['password'] != postData['confpass']:
            errors.append("Password does not match password confirmation.")
        return errors
    def loginvalidation(self, postData):
        errors = []
        loginuser = Users.objects.filter(email=postData['email'])
        if loginuser:
            passtest = loginuser[0].password.encode()
        if not loginuser or bcrypt.hashpw(postData['password'].encode(), passtest) != passtest:
            errors.append("Invalid login")
        return errors


class Users(models.Model):
    first = models.CharField(max_length = 100)
    last = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)
    permission = models.IntegerField()
    admin_request = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Events(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    rate = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    event_creator = models.ForeignKey(Users, related_name="user_creator")
    image = models.FileField(upload_to = "uploads/events")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Genres(models.Model):
    genre = models.CharField(max_length = 100)
    event_genre = models.ManyToManyField(Events)

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.FileField(upload_to = "uploads/products")

class Orders(models.Model):
    event = models.ManyToManyField(Events, related_name = "event_order")
    product = models.ManyToManyField(Products, related_name = "product_order")
    user = models.ForeignKey(Users, related_name = "user_order")
    ship_number = models.IntegerField()
    ship_street = models.CharField(max_length=100)
    ship_unit = models.CharField(max_length=100)
    ship_city = models.CharField(max_length=100)
    ship_state = models.CharField(max_length=10)
    ship_zip = models.IntegerField()
