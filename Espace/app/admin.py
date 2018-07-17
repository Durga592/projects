# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import Ecourse, Ehall, Eexpenses, Estudent, Eenquiry
# Register your models here.
admin.site.register(Ecourse)
admin.site.register(Ehall)
admin.site.register(Eexpenses)
admin.site.register(Estudent)
admin.site.register(Eenquiry)
