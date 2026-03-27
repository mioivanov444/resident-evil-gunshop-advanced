from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.conf import settings
from .models import Profile
from django.contrib.auth.models import Group, Permission

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()


@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    # Moderator
    admin_group, _ = Group.objects.get_or_create(name='Moderator')

    # Regular users
    user_group, _ = Group.objects.get_or_create(name='User')

    # Moderator permissions
    gun_perms = Permission.objects.filter(content_type__app_label='guns')
    category_perms = Permission.objects.filter(content_type__app_label='guns')
    review_perms = Permission.objects.filter(content_type__app_label='reviews')

    admin_group.permissions.set(gun_perms | category_perms | review_perms)

    # User review permissions
    user_group.permissions.set(review_perms)