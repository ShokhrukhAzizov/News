from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.PositiveIntegerField(blank=True, null=True)
    

    class Meta(AbstractUser.Meta):
        swappable ='AUTH_USER_MODEL'
        verbose_name='User'
        verbose_name_plural='Users'
    
class Region(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)

    def __str__(self):
        return self.title

  

class News(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255,unique=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'
        ordering = ('-created_at',)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    news = models.ForeignKey(News,on_delete=models.CASCADE)


class Views(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    # people = models.ForeignKey(User,on_delete=models.DO_NOTHING)
