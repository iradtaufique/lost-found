from django.db import models
from django.db.models.base import Model
from django.conf import settings
import documents

# Create your models here.

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    type = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.type


class Policepost(models.Model):
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.location


class Idcollection(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    idnumber = models.CharField(max_length=200)
    first_name = models.CharField(max_length=225, default='First_name')
    second_name = models.CharField(max_length=225, default='second_name')
    district = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to="image", default='image/download.png')
    isfound = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    documentType = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    location = models.ForeignKey(
        Policepost, on_delete=models.SET_NULL, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.idnumber}'

    class Meta:
        ordering = ['isfound']

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


# class Comment(models.Model):
#     comment = models.ForeignKey(Idcollection, on_delete=models.CASCADE)
#     names = models.CharField(max_length=25)
#     body = models.TextField()
#     time_stamp = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.comment
