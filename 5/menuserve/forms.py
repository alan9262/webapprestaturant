from django import forms
from .models import Item,Store, Manager, Employee, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MenuForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'item_name',
            'content_description',
            'price',
            'featured',
            'image'
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

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username'
        ]

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user