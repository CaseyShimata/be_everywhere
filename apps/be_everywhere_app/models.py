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
        if postData['password'] != postData['confirm_password']:
            errors.append("Password does not match password confirmation.")
        if errors:
            return {'errors':errors}
        else:
            hashpass = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = Users.objects.create(first=postData['first'], last=postData['last'], email=postData['email'], password=hashpass, permission=3, admin_request=False)
            return {'theuser':user}
    def loginvalidation(self, postData):
        errors = []
        password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

        try:
            user = Users.objects.get(email=postData['email'])
        except:
            errors.append("Invalid user!")
            return {'errors':errors}

        if not bcrypt.hashpw(postData['password'].encode(), user.password.encode()) == user.password.encode():
            errors.append("Wrong Password!")

        if errors:
            return {'errors':errors}
        else:
            return {'theuser':user}

class EventsManager(models.Model):
    def new(self, postData, id):
        errors = []
        if len(postData['name']) < 2:
            errors.append("Name must be at least 2 character.")
        if len(postData['location']) < 2:
            errors.append("Location must be at least 2 character.")
        if len(postData['genre']) < 1:
            errors.append("Please enter a genre.")
        if len(postData['start_date']) < 1:
            errors.append("Enter a start date")
        elif datetime.strptime((postData['start_date']), '%Y-%m-%d') < datetime.now():
            errors.append("Start date must be in the future!")
        if len(postData['end_date']) < 1:
            errors.append("Enter an end date")
        elif datetime.strptime((postData['end_date']), '%Y-%m-%d') < datetime.strptime((postData['start_date']), '%Y-%m-%d'):
            errors.append("End date must be after the start date!")
        if errors:
            return {'errors':errors}
        else:
            Events.objects.create(name=postData['name'], location=postData['location'], description=postData['description'], rate=postData['rate'], start_date=datetime.strptime((postData['start_date']), '%Y-%m-%d'), end_date=datetime.strptime((postData['end_date']), '%Y-%m-%d'), event_creator=id, status=True, image='dummy.png' )

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
    status = models.BooleanField()
    image = models.FileField(upload_to = "uploads/events")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EventsManager()

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
