# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import serializers
from rest_framework import generics
from django_filters import filters

from users.models import User


class UserFilter(filters.FilterSet):

    name = filters.CharFilter(name='name', lookup_expr='iexact')

    class Meta:
        model = User
        fields = (
            'name',
        )


class UserDetail(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            'name',
        )


class UserList(generics.ListAPIView):
    name = 'user-list'
    queryset = Users.objects.all()
    serializer_class = UserDetail
