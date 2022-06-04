from django.shortcuts import render
from galerie.models import Painting, Author, Attachment
from django.views.generic import ListView, DetailView


def index(request):
    num_paintings = Painting.objects.all().count()
    num_authors = Author.objects.all().count()
    paintings = Painting.objects.order_by('year')[:4]

    context = {
        'nadpis': 'Galerie',
        'paintings': paintings,
        'authors': Author,
        'num_paintings': num_paintings,
        'num_authors': num_authors
    }

    return render(request, 'index.html', context=context)


class PaintingListView(ListView):
    model = Painting
    context_object_name = 'paintings_list'
    template_name = 'painting/list.html'


class PaintingDetailView(DetailView):
    model = Painting
    context_object_name = 'painting_detail'
    template_name = 'painting/detail.html'