# encoding: utf-8
__author__ = 'fanzhikang'
__date__ = '2018/9/30 14:19'

from rest_framework import serializers
from .models import Post, Tag
from django.contrib.auth.models import User

class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ('url', 'id', 'title', 'pub_time', 'author', 'body', 'tags')

class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ('url', 'id', 'name', 'posts')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'posts')