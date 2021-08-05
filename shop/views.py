from django.shortcuts import render, get_object_or_404
from .models import ShopBasket
# Create your views here.


def index(request):

    item_list = ShopBasket.objects.filter(s_ordered=True).order_by('-id')[:5]
    context = {
        "item": item_list
    }
    return render(request, 'shop/index.html', context)
