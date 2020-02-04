from django.shortcuts import render, get_object_or_404, redirect
from .forms import MenuForm, StoreForm, OrderForm, EmployeeForm, ManagerForm, RegistrationForm, UserForm
from .models import Item, Store, Order, Manager, Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import collections
from django import forms

@login_required
def get(request):
    return render(request, 'menuserve/manage.html' )

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                posts = Item.objects.all()
                context = {'posts': posts}
                return render(request, 'menuserve/index.html', context)
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/login.html', context)

def index(request):
    posts = Item.objects.all()
    return render(request, 'menuserve/index.html', {'posts': posts})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            user = request.user
            username = request.POST.get('username')
            password = request.POST.get('password1')
            group = Group.objects.get(name='Customers')
            users = User.objects.get(username=username)
            users.groups.add(group)
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/')
    else:
        form = RegistrationForm()
        context = {
            'form': form
        }
        return render(request, 'menuserve/register.html', context)

def order(request):
    form = OrderForm(request.POST or None)
    form.save()
    posts = Item.objects.filter(user=request.user)
    stores = Store.objects.all()
    context={
        'posts': posts,
        'stores': stores
    }
    return render(request, 'menuserve/orderPage.html', context)

def addorder(request):
    totalamount = float(0.0)
    form = OrderForm(request.POST or None)
    itemList = Item.objects.all()
    storeList = Store.objects.all()
    items = ""
    print(form)
    #item_name = form.order_items.item_name
    if form.is_valid():
        for pr in itemList:
            totalamount = float(totalamount + float(pr.price))
        totalamount = float(totalamount * float(request.POST.get('quantity')))
        form.save()
        form = OrderForm()
    stores = Store.objects.all()
    user = request.user
    context={
        'form': form,
        'itemList': itemList,
        'stores': storeList,
        'totalamount': totalamount,
        'user': user
    }
    return render(request, 'menuserve/addOrder.html', context)

def orderHistory(request):
    totalamount = float(0.0)
    form = OrderForm(request.POST or None)
    posts = Item.objects.all()
    orders = Order.objects.all()
    if form.is_valid():
        for pr in posts:
            totalamount = float(totalamount + float(pr.price))
        totalamount = float(totalamount * float(request.POST.get('quantity')))
    context={
        'form': form,
        'posts': posts,
        'orders': orders,
        'totalamount': totalamount
    }
    return render(request, 'menuserve/orderHistory.html', context) 

@login_required
def manage(request):
    posts = Item.objects.all()
    return render(request, 'menuserve/manage.html', {'posts': posts})

def about(request):
    return render(request, 'menuserve/about.html', {})

@login_required
def menu_form(request):
    form = MenuForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        form = MenuForm()
    context = {
        'form': form
    }
    return render(request, "menuserve/itemCreate.html", context)

def edit_store(request):
    form = StoreForm(request.POST or None)
    stores = Store.objects.all()
    if form.is_valid():
        form.save()
        form = StoreForm()
        stores = Store.objects.all()
    context = {
        'form': form,
        'stores': stores
        }
    return render(request, "menuserve/storesEdit.html", context)

def edit_employee(request):
    form = EmployeeForm(request.POST or None)
    employees = Employee.objects.all()
    if form.is_valid():
        form.save()
        form = EmployeeForm()
        employees = Employee.objects.all()
    context = {
        'form': form,
        'employees': employees
        }
    return render(request, "menuserve/employeeEdit.html", context)
    
def edit_users(request):
    employees = User.objects.filter(groups__name='Employees')
    customers = User.objects.filter(groups__name='Customers')
    form = ManagerForm(request.POST or None)
    form2 = UserForm(request.POST or None)
    managers = User.objects.filter(groups__name='Managers')
    if form.is_valid():
        form.save()
        form2.save()
        form = ManagerForm()
        form2 = UserForm()
        managers = User.objects.filter(groups__name='Managers')
    context = {
        'form': form,
        'form2': form2,
        'managers': managers,
        'employees': employees,
        'customers': customers
        }
    return render(request, "menuserve/editUsers.html", context)

def edit_manager(request):
    form = ManagerForm(request.POST or None)
    form2 = UserForm(request.POST or None)
    managers = User.objects.filter(groups__name='Managers')
    if form.is_valid():
        form.save()
        form2.save()
        form = ManagerForm()
        form2 = UserForm()

        managers = User.objects.filter(groups__name='Managers')
    context = {
        'form': form,
        'form2': form2,
        'managers': managers
        }
    return render(request, "menuserve/managerEdit.html", context)

def edit_menu(request, id):
    obj = get_object_or_404(Item, id=id)
    if request.method == "POST":
        form = MenuForm(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            posts = Item.objects.get(id=id)
            context = {'form': form, 'posts': posts}
            return redirect("/", context)
    else:
        form = MenuForm(instance=obj)
        context={ 'form': form }
        return render(request, "menuserve/itemEdit.html", context)

def store_edit(request, id):
    obj = get_object_or_404(Store, id=id)
    if request.method == "POST":
        form = StoreForm(request.POST, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save()
            stores = Store.objects.all()
            return redirect("/", {'stores': stores})
    else:
        form = StoreForm(instance=obj)
        context={ 'form': form }
        return render(request, "menuserve/storesEdit.html", context)

def employeeedit(request, id):
    obj = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            employees = Employee.objects.all()
            return redirect("/", {'employees': employees})
    else:
        form = EmployeeForm(instance=obj)
        context={ 'form': form }
        return render(request, "menuserve/employeeEdit.html", context)

def manageredit(request, id):
    obj = get_object_or_404(User, id=id)
    print(obj)
    if request.method == "POST":
        form = UserForm(instance=obj)
        print(form)
        if form.is_valid():
            instance = ManagerForm.save(commit=False)
            form.save()
            managers = User.objects.filter(groups__name='Managers')
            context={ 
                'form': form,
                'user': obj,
                'managers': managers
            }
            return render(request, "menuserve/managerEdit.html", context)
    else:
        form = ManagerForm(instance=obj)
        context={ 
            'form': form,
            'user': obj
         }
        return render(request, "menuserve/managerEdit.html", context)

def itemdelete(request, id):
    obj = get_object_or_404(Item, id=id)
    obj.delete()
    posts = Item.objects.all()
    return render(request, "menuserve/manage.html", {'posts': posts})

def storedelete(request, id):
    print(request)
    obj = get_object_or_404(Store, id=id)
    obj.delete()
    stores = Store.objects.all()
    form = StoreForm()
    context = {
        'form': form,
        'stores': stores
    }
    return redirect("/", context)

def employeedelete(request, id):
    print(request)
    obj = get_object_or_404(Employee, id=id)
    obj.delete()
    employees = Employee.objects.all()
    form = EmployeeForm()
    context = {
        'form': form,
        'employees': employees
    }
    return redirect("/", context)

def managerdelete(request, id):
    print(request)
    obj = get_object_or_404(Manager, id=id)
    obj.delete()
    managers = Manager.objects.all()
    form = ManagerForm()
    context = {
        'form': form,
        'managers': managers
    }
    return redirect("/", context)

def fulfilorder(request, id):
    obj = get_object_or_404(Order, id=id)
    obj.delete()
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return redirect("/", context)