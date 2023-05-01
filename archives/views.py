from django.http import Http404
from django.shortcuts import render
from django.contrib import messages


from archives.models import Animal

# Create your views here.


def get_all_animals(request):
    all_animals = Animal.objects.all()

    context = {
        'all_animals_list': all_animals
    }

    return render(request, 'index.html', context)


def get_animal(request, animal_id):

    try:
        animal = Animal.objects.get(id=animal_id)
    except Animal.DoesNotExist:
        raise Http404('Lost, ehh?')
    context = {}
    if animal:
        context.update({'animal': animal})
    return render(request, 'animal.html', context)
