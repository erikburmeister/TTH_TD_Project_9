from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

def menu_list(request):
    menus = Menu.objects.filter(
        expiration_date__gte=timezone.now()).order_by(
        'expiration_date').prefetch_related('items')
    return render(request,
                  'menu/menu_home.html',
                  {'menus': menus, 'title': 'Home'})


def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu/menu_detail.html',
                  {'menu': menu, 'title': 'Menu Detail'})


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'menu/detail_item.html',
                  {'item': item, 'title': 'Item Detail'})


def create_new_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST)

        if form.is_valid():
            menu = form.save(commit=False)
            menu.created_date = timezone.now()
            menu.save()
            form.save_m2m()
            return redirect('menu_detail', pk=menu.pk)

    else:
        form = MenuForm()

    return render(request, 'menu/menu_edit.html',
                  {'form': form, 'title': 'Create New Menu'})


def edit_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    form = MenuForm(request.POST or None, instance=menu)

    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)

        if form.is_valid():
            menu = form.save(commit=False)
            menu.created_date = timezone.now()
            menu.save()
            form.save_m2m()
            return redirect('menu_list')

    return render(request,
                  'menu/menu_edit.html',
                  {'form': form, 'title': 'Edit Menu'})