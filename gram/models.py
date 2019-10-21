from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Post(models.Model):
    post_image = models.ImageField(upload_to = 'photos/')
    post_caption = models.CharField(max_length=300)
    upload_by = models.CharField(max_length =30)

    def __str__(self):
        return self.caption

    def save_photo(self, user):
        self.save()

    @classmethod
    def all_photos(cls):
        all_photos = cls.objects.all()
        return all_photos

    @classmethod
    def user_photos(cls, username):
        photos = cls.objects.filter(uploaded_by__username=username)
        return photos

    @classmethod
    def filter_by_caption(cls, search_term):
        return cls.objects.filter(caption__icontains=search_term)

    def delete_photo(self, user):
        self.delete()
        
class Comment(models.Model):
    comment_content = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post_comment = models.ForeignKey(Post,on_delete=models.CASCADE)

    def save_comment(self):
        self.save()
    


