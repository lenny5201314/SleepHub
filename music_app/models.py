from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from .utils import unique_music_id_generator
# Create your models here.
class UserProfileInfo(models.Model):
    sex_SIZES = (("男","男"),("女","女"))
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=2, choices=sex_SIZES,blank=False)
    # Add any additional attributes you want
    #portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    #profile_pic = models.ImageField(upload_to='basic_app/profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
class record_user_click(models.Model):
    user_id = models.IntegerField()
    musicid = models.CharField(max_length=120)
    session_id = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class MusicfileInfo(models.Model):
    category_SIZES = (("自然","自然"),("動物","動物"),("人","人"),("室內","室內"),("旋律","旋律"),("技術","技術"))
    title = models.CharField(max_length=100)
    description= models.TextField(blank=True)
    music = models.FileField(upload_to='musics/')
    music_pic = models.ImageField(upload_to='image/',blank=True)
    musiccategory = models.CharField(max_length=12, choices=category_SIZES)
    music_tag = models.CharField(max_length=120,blank=True)
    musicid = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Add any additional attributes you want
    #portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    #profile_pic = models.ImageField(upload_to='basic_app/profile_pics',blank=True)

    def __str__(self):
        return self.title

def pre_save_music_id(instance, sender, *args, **kwargs):
    if not instance.musicid:
        instance.musicid= unique_music_id_generator(instance)


pre_save.connect(pre_save_music_id, sender= MusicfileInfo)
