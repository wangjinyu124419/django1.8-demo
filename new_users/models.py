# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


# Create your models here.
class CmsUser(AbstractUser):
    pass

class CmsGroup(Group):
   pass