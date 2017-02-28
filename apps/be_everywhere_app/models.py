from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    first = models.CharField(max_length = 100)
    last = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)
    permission = models.IntegerField()
    admin_request = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
