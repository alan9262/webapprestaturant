from django.contrib import admin
from .models import Item, Employee, Store, Order, Manager

admin.site.register(Item)

admin.site.register(Employee)

admin.site.register(Store)

admin.site.register(Order)

admin.site.register(Manager)
