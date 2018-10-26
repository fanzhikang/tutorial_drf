from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pub_time',)

class Tag(models.Model):

    name = models.CharField(max_length=50)



