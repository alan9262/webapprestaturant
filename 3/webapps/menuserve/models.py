from django.db import models

# Create your models here.
# Indentation of fields and their datatypes for easy readability

class Item(models.Model):
    item_name           = models.CharField(max_length=60)
    content_description = models.TextField(blank=True, null=True)
    price               = models.DecimalField(decimal_places =2, max_digits = 1000)
    featured            = models.BooleanField(null=True)
    class Meta:
        verbose_name = ('Item')
        verbose_name_plural = ('Items')
    def __str__(self):
        return self.item_name

class Store(models.Model):
    store_name           = models.CharField(max_length=40)
    location             = models.CharField(max_length=40)
    class Meta:
        verbose_name = ('Store')
        verbose_name_plural = ('Stores')
    def __str__(self):
        return self.store_name
        
class Manager(models.Model):
    manager_name           = models.CharField(max_length=40, default="Manager", blank=True, null=True)
    location               = models.ManyToManyField(Store)
    class Meta:
        verbose_name = ('Manager')
        verbose_name_plural = ('Managers')
    def __str__(self):
        return self.manager_name

class Employee(models.Model):
    employee_name           = models.CharField(max_length=40, default="Employee", blank=True, null=True)
    location                = models.ManyToManyField(Store, blank=True)
    position                = models.CharField(max_length=40, blank=True, null=True)
    manager_name            = models.ForeignKey(Manager, on_delete=models.CASCADE)
    class Meta:
        verbose_name = ('Employee')
        verbose_name_plural = ('Employees')
    def __str__(self):
        return self.employee_name

class Order(models.Model):
    order_items           = models.ManyToManyField(Item)
    quantity              = models.IntegerField(blank=False, default=1)
    price                 = models.DecimalField(decimal_places =2, max_digits = 1000, default=0)
    store                 = models.ForeignKey(Store, on_delete=models.CASCADE)
    fulfil                = models.BooleanField(default=False)
    class Meta:
        verbose_name = ('Order')
        verbose_name_plural = ('Orders')
    def __str__(self):
        return str(self.order_items)