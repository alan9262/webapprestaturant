from django import forms
from .models import Item,Store, Manager, Employee, Order

class MenuForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'item_name',
            'content_description',
            'price'
        ]

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'store_name',
            'location'
        ]

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = [
            'manager_name',
            'location'
        ]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'employee_name',
            'location',
            'position',
            'manager_name'
        ]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'order_items',
            'quantity',
            'store'
        ]