from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import inventory, Item


@login_required
def homepage(request):
    inv = inventory.objects.all()

    for each in inv:
        items = Item.objects.filter(item=each)
        each.total = len(items)
        each.save()

    context = {
        'inventory': inv,
    }
    return render(request, 'inventory/home.html', context)

@login_required
def list_view(request, item_id):
    item = Item.objects.filter(item=item_id)
    inv = inventory.objects.get(pk=item_id)
    context = {
        'list_items': item,
        'inv': inv,
        'item_id': item_id
    }

    return render(request, 'inventory/list.html', context)

@login_required
def add_inventory(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            inv = inventory()
            inv.inv_class = request.POST.get('name')
            inv.total = 0
            inv.save()
            inv = inventory.objects.all()
            for each in inv:
                items = Item.objects.filter(item=each)
                each.total = len(items)
                each.save()
            context = {
                'inventory': inv,
            }
            return redirect('/inventory/homepage/', context)
        else:
            inv = inventory.objects.all()
            for each in inv:
                items = Item.objects.filter(item=each)
                each.total = len(items)
                each.save()
            context = {
                'inventory': inv,
            }
            return redirect('/inventory/homepage/', context)

@login_required
def add_item(request, item_id):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('price') and request.POST.get('quantity') and request.POST.get(
                'status'):
            if request.POST.get('status') == 'Available' or request.POST.get(
                    'status') == 'Need Restocking' or request.POST.get('status') == 'SOLD':
                element = Item()
                element.item = inventory.objects.get(pk=item_id)
                element.item_name = request.POST.get('name')
                element.item_price = int(request.POST.get('price'))
                element.total_no = int(request.POST.get('quantity'))
                element.status = request.POST.get('status')
                element.save()
                item = Item.objects.filter(item=item_id)
                inv = inventory.objects.get(pk=item_id)
                context = {
                    'list_items': item,
                    'inv': inv,
                    'item_id': item_id
                }
                url = '/inventory/' + str(item_id) + '/listview/'
                return redirect(url, context)
            else:
                item = Item.objects.filter(item=item_id)
                inv = inventory.objects.get(pk=item_id)
                context = {
                    'list_items': item,
                    'inv': inv,
                    'item_id': item_id,
                    'error': 'ENTER CORRRECT-LY'
                }
                return render(request, 'inventory/list.html', context)

        else:
            item = Item.objects.filter(item=item_id)
            inv = inventory.objects.get(pk=item_id)
            context = {
                'list_items': item,
                'inv': inv,
                'item_id': item_id,
                'error': 'ENTER CORRRECT-LY'
            }
            return render(request, 'inventory/list.html', context)

@login_required
def delete_item(request, item_pk):
    element = Item.objects.get(pk=item_pk)
    item_id = element.item
    element.delete()

    item = Item.objects.filter(item=item_id)
    inv = item_id
    context = {
        'list_items': item,
        'inv': inv,
        'item_id': item_id.pk
    }
    url = '/inventory/' + str(item_id.pk) + '/listview/'
    return redirect(url, context)

@login_required
def edit_item(request, item_pk):
    unique = get_object_or_404(Item, pk=item_pk)
    context = {
        'item': unique,
        'item_pk': item_pk
    }
    return render(request, 'inventory/edit_item.html', context)

@login_required
def edit_save(request, item_pk):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('price') and request.POST.get('quantity') and request.POST.get(
                'status'):
            if request.POST.get('status') == 'Available' or request.POST.get(
                    'status') == 'Need Restocking' or request.POST.get('status') == 'SOLD':
                element = Item.objects.get(pk=item_pk)
                item_id = element.item.pk
                element.delete()

                element = Item()
                element.item = inventory.objects.get(pk=item_id)
                element.item_name = request.POST.get('name')
                element.item_price = int(request.POST.get('price'))
                element.total_no = int(request.POST.get('quantity'))
                element.status = request.POST.get('status')
                element.save()
                item = Item.objects.filter(item=item_id)
                inv = inventory.objects.get(pk=item_id)
                context = {
                    'list_items': item,
                    'inv': inv,
                    'item_id': item_id
                }
                url = '/inventory/' + str(item_id) + '/listview/'
                return redirect(url, context)
            else:
                element = Item.objects.get(pk=item_pk)
                item_id = element.item.pk
                item = Item.objects.filter(item=item_id)
                inv = inventory.objects.get(pk=item_id)
                context = {
                    'list_items': item,
                    'inv': inv,
                    'item_id': item_id,
                    'error': 'ALL THE ENTRIES WERE NOT CORRECT EDIT AGAIN'
                }
                return render(request, 'inventory/list.html', context)

        else:
            element = Item.objects.get(pk=item_pk)
            item_id = element.item.pk
            item = Item.objects.filter(item=item_id)
            inv = inventory.objects.get(pk=item_id)
            context = {
                'list_items': item,
                'inv': inv,
                'item_id': item_id,
                'error': 'INCOMPLETE INFORMATION EDIT AGAIN'
            }
            return render(request, 'inventory/list.html', context)
