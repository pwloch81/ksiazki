import requests
from django.shortcuts import render
from rest_framework import filters, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .fields import ksiazkiForm
from .models import ksiazki
from .serializer import ksiazkiSerializer


# Create your views here.

def importzAPI(request):
    slow = {}
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=search+terms').json()
    dict = response['items']

    for i in range(len(dict)):
        for key, value in dict[i]['volumeInfo'].items():
            if key == 'title':
                slow['tytuł'] = value
            elif key == 'authors':
                slow['autor'] = value
            elif key == 'publishedDate':
                if len(value) < 10:
                    if len(value) < 7:
                        value = value + '-02-02'
                    else:
                        value = value + '-02'
                slow['data'] = value
            elif key == 'pageCount':
                slow['strony'] = value
            elif key == 'language':
                slow['jezyk'] = value
            elif key == 'imageLinks':
                slow['link'] = value
            elif key == 'id':
                slow['ISBN'] = value

        models = ksiazki(tytuł=slow['tytuł'], autor=slow['autor'], data=slow['data'], jezyk=slow['jezyk'],
                         strony=slow['strony'], link=slow['link'])
        models.save()
    return render(request, 'ksiazka/importzAPI.html', {'response': slow})


def index(request):
    if 'a' in request.GET:
        a = request.GET['a']
        ksiazka = ksiazki.objects.filter(tytuł__icontains=a)
    elif 'b' in request.GET:
        b = request.GET['b']
        print(b)
        ksiazka = ksiazki.objects.filter(autor__icontains=b)
    elif 'c' in request.GET:
        c = request.GET['c']
        print(c)
        ksiazka = ksiazki.objects.filter(jezyk__icontains=c)

    elif 'd' in request.GET and 'e' in request.GET:
        d = request.GET['d']
        e = request.GET['e']
        ksiazka = ksiazki.objects.filter(data__range=[d, e])
    else:
        ksiazka = ksiazki.objects.all()
    # ksiazka = ksiazki.objects.all()

    dane = {'ksiazka': ksiazka}
    print(request.user)
    return render(request, 'ksiazka/szablon.html', dane)


def ksiazka_formularz(request):
    form = ksiazkiForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = ksiazkiForm()
    context = {'form': form}
    return render(request, 'ksiazka/dodaj_ksiazke.html', context)


def search(request):
    tytuł = request.GET.get('tytuł')
    print(tytuł)
    print(request.user)
    return render(request, 'ksiazka/search.html', {})


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list': '/task-list/',
        'Detail view': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-updte/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def ksiazkiList(request):
    ksiazkie = ksiazki.objects.all()
    serializer = ksiazkiSerializer(ksiazkie, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ksiazkiszczegolowo(request, pk):
    ksiazkie = ksiazki.objects.get(id=pk)
    serializer = ksiazkiSerializer(ksiazkie, many=False)
    return Response(serializer.data)


class UserListView(generics.ListAPIView):
    queryset = ksiazki.objects.all()
    serializer_class = ksiazkiSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=tytuł', 'autor', 'jezyk', 'ISBN']
