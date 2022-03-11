import os
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

def rename_img_video(instance, filename):
    ext = filename.split('.')[-1]
    name = ''
    for i in range((len(filename.split('.'))-1)):
        name += filename.split('.')[i]
    filename = f"{name}_{instance.date_updated}.{ext}"
    if ext.lower() in ['png', 'jpg', 'gif']:
        return os.path.join(f'{instance.author.first_name}/image_post', filename)
    return os.path.join(f'{instance.author.first_name}/video_post', filename)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    message = models.TextField(_("message"), blank=True)
    video = models.FileField(_("video"), upload_to=rename_img_video, blank=True, null=True)
    img = models.ImageField(_("image"), upload_to=rename_img_video, blank=True, null=True)
    date_created = models.DateTimeField(_("date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("date updated"), auto_now=True)
    likes = models.ManyToManyField(User, related_name='user_like', blank=True)

    def __str__(self):
        return f"{self.author.first_name}"
    
    def total_likes(self):
        return self.likes.count()
    
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-date_updated',)