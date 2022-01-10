from django.db import models

# Create your models here.


class Order(models.Model):
    names = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    document = models.CharField(max_length=225)
    message = models.TextField()
    created_on = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.names


class Contact_us(models.Model):
    names = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    message = models.TextField()
    created_on = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.names
