from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    price = models.SmallIntegerField(blank=True, null=True)
    capacity = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    hours = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    menu_up = models.FileField(null=True, blank=True, upload_to='uploads/menus')
    menu = models.FilePathField(path='uploads/menus', recursive=False, max_length=100, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True)
    logo_up = models.ImageField(null=True, blank=True, upload_to='logos')

    def __str__(self):
        return self.name
