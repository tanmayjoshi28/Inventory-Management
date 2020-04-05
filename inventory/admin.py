from django.contrib import admin
from .models import inventory, Item

admin.site.register(inventory)
admin.site.register(Item)
