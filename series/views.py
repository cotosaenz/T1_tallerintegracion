from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

# Create your views here.

def index(request):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad') #revisar si puedo hacer esto afuera y dsps pasarlo como parametro a las funciones!
    bblist = response.json()
    bb_total = int(bblist[-1]['season'])
    bb_seasons = []
    for i in range(1, bb_total+1):
        bb_seasons.append(i)
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
    bcslist = response.json()
    bcs_total = int(bcslist[-1]['season'])
    bcs_seasons = []
    for i in range(1, bcs_total+1):
        bcs_seasons.append(i)
    return render(request, 'series/index.html', {'bb':bb_seasons, 'bcs':bcs_seasons})

def bb_season(request, id_season):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
    lista = response.json()
    episodes = []
    for episode in lista:
        if episode['season'] == str(id_season):
            episodes.append(episode)
    return render(request, 'series/show_temporada.html', {'list':episodes})

def bcs_season(request, id_season):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
    lista = response.json()
    episodes = []
    for episode in lista:
        if episode['season'] == str(id_season):
            episodes.append(episode)
    return render(request, 'series/show_temporada.html',{'list':episodes})

def episode(request, id_episode):
    link = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/'+str(id_episode)
    response = requests.get(link)
    lista = response.json()
    lista[0]['air_date'] = lista[0]['air_date'][0:10]
    return render(request, 'series/show_episode.html',{'list':lista[0]})

def character(request, character):
    name = character.split(" ")
    if len(name) == 3:
        link = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(name[0])+'+'+str(name[1])+'+'+str(name[2])
    elif len(name) == 2:
        link = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(name[0])+'+'+str(name[1])
    else:
        link = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(name[0])
    response = requests.get(link)
    lista = response.json()
    return render(request, 'series/show_character.html', {'list':lista[0]})

def search(request):
    query = request.GET.get('q')
    name = query.split(" ")
    if len(name) == 1 and name[0] != '':
      link = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(name[0])
      response = requests.get(link)
      lista = response.json()
    elif len(name) == 2:
      link = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(name[0])+'+'+str(name[1])
      response = requests.get(link)
      lista = response.json()
    elif len(name) == 3:
      link = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(name[0])+'+'+str(name[1])+'+'+str(name[2])
      response = requests.get(link)
      lista = response.json()
    else:
      lista = []
    return render(request, 'series/results_search.html',{'list': lista})


