from typing import List

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import ItemForm
from .models import Item


# Create your views here
def index(request):
    item_list: List[Item] = Item.objects.all()
    template = loader.get_template("food/index.html")
    context = {
        "item_list": item_list,
    }
    return render(
        request=request,
        template_name="food/index.html",
        context=context
    )


def item(request):
    return HttpResponse("<h1>This is an item view</h1>")


def detail(request, item_id: int):
    item = Item.objects.get(pk=item_id)
    context = {
        "item": item
    }
    return render(
        request=request,
        template_name="food/detail.html",
        context=context
    )


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")

    context = {
        "form": form
    }
    return render(
        request=request,
        template_name='food/item-form.html',
        context=context
    )


def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    context = {
        "form": form
    }
    return render(
        request,
        "food/item-form.html",
        context=context
    )


def delete_item(request, item_id: int):
    item = Item.objects.get(pk=item_id)

    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    context = {
        "item": item
    }
    return render(
        request,
        "food/item-delete.html",
        context

    )
