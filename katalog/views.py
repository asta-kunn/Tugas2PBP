# jelasin
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    item_katalog = CatalogItem.objects.all()
    context = {                             
        'item_katalog': item_katalog,
        'nama' : 'Rifqi',
        'student_id' : '2106752224'
    }
    return render(request, 'katalog.html', context)
