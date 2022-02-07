from django.db import models

# Create your models here.

class Room(models.Model):
    # host
    # topic
    name = models.CharField(max_length=200)
    # TextField: bigger than CharField
    # null: can be null in database
    # blank: form data can be blank whether add or update it
    description = models.TextField(null=True, blank=True)
    # participants
    updated = models.DateTimeField(auto_now=True) # every saving time
    created = models.DateTimeField(auto_now_add=True) # only when first created

    def __str__(self) -> str:
        return self.name