from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from .models import Person


@receiver(post_save, sender=User) 
def create_person(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(django_username=instance)


@receiver(post_save, sender=User)
def save_person(sender, instance, **kwargs):
    instance.person.save()

