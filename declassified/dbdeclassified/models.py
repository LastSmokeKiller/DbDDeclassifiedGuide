from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Group


class MyUserManager(BaseUserManager):
    """Create a new user profile"""
    def create_user(self, email, username, password=None):
        """Creates and saves a User with the given email, username, name, and password"""

        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username = username
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, username, password):
        """Creates and save a superuser with the given email, username and password"""
        user = self.create_user(email,username,password)

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique = True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    """These are the methods for all of the porperties in the class, which allows retrival of properties for pages"""

    def get_username(self):
        """Returns username"""
        return self.username
    
    def get_email(self):
        """Returns email"""
        return self.email
    
    def __str__(self):
        """This is the to string that returns the email of the user"""
        return self.email
    
    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True
        

"""
The Profile class stores information about the user. This will allow users to gameplay hours,
profile picture, associated game profiles, self ranking, and about me information.
Every User object is bound to only one profile. On deletion of a User, the Profile is also disposed of.
"""

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    gameplay_hours =  models.IntegerField(max_length=100000000, default=0)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='img\profile', default='Meg.jpg')


    def get_profile_picture(self):
        return self.profile_picture

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    """Methods allow for the updating of files to our database for the profile pictures."""
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
