# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import serializers
from rest_framework import generics
from users.models import User


class UserDetail(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            'name',
        )


class UserList(generics.ListAPIView):
    name = 'user-list'
    serializer_class = UserDetail

    def get_queryset(self):
        name = self.kwargs.get('name')
        return User.objects.filter(name=name)