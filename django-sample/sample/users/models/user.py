# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Guardamos el nombre del usuario siempre en minusculas.

        self.name = self.name.lower()
        self.full_clean()

        return super(User, self).save(*args, **kwargs)
