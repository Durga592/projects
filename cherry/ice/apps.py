# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class IceConfig(AppConfig):
    name = 'ice'

    def ready(self):
    	from ice.signals import save_profile, get_details
