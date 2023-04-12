from django.shortcuts import render
from django.db.models import Q
from store.models.product import Products

def search(request):
    query = request.GET.get('q')
    if query:
        products = Products.objects.filter(Q(name__icontains=query) | Q(author__icontains=query))
    else:
        products = Products.objects.all()
    return render(request, 'searchbar.html', {'products': products})


