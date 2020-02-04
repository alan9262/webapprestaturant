from django.shortcuts import render, get_object_or_404, redirect
from .forms import MenuForm, StoreForm, OrderForm, EmployeeForm, ManagerForm
from .models import Item, Store, Order, Manager, Employee
import collections

def get(request):
    return render(request, 'menuserve/manage.html', )

def index(request):
    posts = Item.objects.all()
    print(posts)
    return render(request, 'menuserve/index.html', {'posts': posts})

def order(request):
    form = OrderForm(request.POST or None)
    form.save()
    posts = Item.objects.all()
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
    #item_name = form.order_items.item_name
    if form.is_valid():
        for pr in itemList:
            totalamount = float(totalamount + float(pr.price))
        totalamount = float(totalamount * float(request.POST.get('quantity')))
        form.save()
        form = OrderForm()
    stores = Store.objects.all()
    context={
        'form': form,
        'itemList': itemList,
        'stores': storeList,
        'totalamount': totalamount
    }
    return render(request, 'menuserve/addOrder.html', context)

def orderHistory(request):
    totalamount = float(0.0)
    form = OrderForm(request.POST or None)
    posts = Item.objects.all()
    orders = Order.objects.all()
    print("-----alan>>")
    print(orders)
    print(request.POST.get('order_items'))
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

def manage(request):
    posts = Item.objects.all()
    return render(request, 'menuserve/manage.html', {'posts': posts})

def about(request):
    return render(request, 'menuserve/about.html', {})

def menu_form(request):
    form = MenuForm(request.POST or None)
    form2 = StoreForm(request.POST or None)
    form3 = EmployeeForm(request.POST or None)
    form4 = ManagerForm(request.POST or None)
    form5 = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MenuForm()
    if form2.is_valid():
        form2.save()
        form2 = StoreForm()
    if form3.is_valid():
        location = request.POST.get('store_name')
        print("location")
        print(location)
        form3.save()
        form3 = EmployeeForm()
    if form4.is_valid():
        form4.save()
        form4 = ManagerForm()
    if form5.is_valid():
        form5.save()
        form5 = OrderForm()
    context = {
        'form': form,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5
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

def edit_manager(request):
    form = ManagerForm(request.POST or None)
    managers = Manager.objects.all()
    if form.is_valid():
        form.save()
        form = ManagerForm()
        managers = Manager.objects.all()
    context = {
        'form': form,
        'managers': managers
        }
    return render(request, "menuserve/managerEdit.html", context)

def edit_menu(request, id):
    obj = get_object_or_404(Item, id=id)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            posts = Item.objects.all()
            return redirect("/", {'posts': posts})
    else:
        form = MenuForm(instance=obj)
        context={ 'form': form }
        return render(request, "menuserve/itemEdit.html", context)

def store_edit(request, id):
    obj = get_object_or_404(Store, id=id)
    if request.method == "POST":
        form = StoreForm(request.POST, instance=obj)
        if form.is_valid():
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
    obj = get_object_or_404(Manager, id=id)
    if request.method == "POST":
        form = ManagerForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            managers = Manager.objects.all()
            return redirect("/", {'managers': managers})
    else:
        form = ManagerForm(instance=obj)
        context={ 'form': form }
        return render(request, "menuserve/managerEdit.html", context)

def itemdelete(request, id):
    print(request)
    print("id here")
    print(id)
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