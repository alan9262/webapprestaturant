from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order', views.addorder, name='order'),
    path('addorder', views.addorder, name='addorder'),
    path('manage', views.manage, name='manage'),
    path('orderhistory', views.orderHistory, name='orderhistory'),
    path('about', views.about, name='about'),
    path('create', views.menu_form, name='create'),
    path('edit_store', views.edit_store, name='edit_store'),
    path('edit_employee', views.edit_employee, name='edit_employee'),
    path('edit_manager', views.edit_manager, name='edit_manager'),
    path('storeedit/<int:id>/edit', views.store_edit, name='storeedit'),
    path('storedelete/<int:id>/delete', views.storedelete, name='storedelete'),
    path('employeeedit/<int:id>/edit', views.employeeedit, name='employeeedit'),
    path('employeedelete/<int:id>/delete', views.employeedelete, name='employeedelete'),
    path('manageredit/<int:id>/edit', views.manageredit, name='manageredit'),
    path('fulfilorder/<int:id>/ok', views.fulfilorder, name='fulfilorder'),
    path('managerdelete/<int:id>/delete', views.managerdelete, name='managerdelete'),
    path('itemedit/<int:id>/edit', views.edit_menu, name='itemedit'),
    path('itemdelete/<int:id>/delete', views.itemdelete, name='itemdelete'),
]