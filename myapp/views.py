from django.shortcuts import render
from .models import Shop

def shop_list(request):
    shops = Shop.objects.select_related('user').all()
    return render(request, 'myapp/shop_list.html', {'shops': shops})

# Create your views here.
