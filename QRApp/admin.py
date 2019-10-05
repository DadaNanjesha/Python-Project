# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Gtin
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.utils.translation import gettext_lazy as _
# Register your models here.


class GtinAdmin(admin.ModelAdmin):
    AdminSite.app_index_title="GTIN Associations"
    AdminSite.site_header="QR-CODE PROJECT"
    list_display = ('gtin_number', 'product_name')
    list_display_links = None
    list_filter = ('gtin_number', 'product_name')
    # class Media:
        

admin.site.register(Gtin, GtinAdmin)
