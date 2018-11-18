# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now

from tinymce.models import HTMLField

import os


# Create your models here.


def upload_share_img(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'share/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )