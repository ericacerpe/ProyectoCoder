from django.shortcuts import render
from django.http import HttpResponse
from Family.models import Familia



# Create your views here.

# def create_family(request):
#     new_person = Familia.objects.create(name='Maria', age=50, has_children=True)
#     print(new_person)
#     return HttpResponse('Se creo el nuevo integrante de la familia')

# def create_family(request):
#      new_person = Familia.objects.create(name='Juan', age=20, has_children=False)
#      print(new_person)
#      return HttpResponse('Se creo el nuevo integrante de la familia')

def create_family(request):
     new_person = Familia.objects.create(name='Hernan', age=45, has_children=True)
     print(new_person)
     return HttpResponse('Se creo el nuevo integrante de la familia')


# Create your views here.

def list_family(request):
    all_perssons =Familia.objects.all()
    print (all_perssons)
    context = {
        'perssons':all_perssons,
    }
    return render(request,'list_family.html', context=context)
