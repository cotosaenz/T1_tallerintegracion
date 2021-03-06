from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests


def index(request):
  try:
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
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
  except Exception as ex: 
    return render(request, 'series/index.html', {'error': ex})

def bb_season(request, id_season):
  try:
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad')
    lista = response.json()
    episodes = []
    for episode in lista:
        if episode['season'] == str(id_season):
            episodes.append(episode)
    return render(request, 'series/show_temporada.html', {'list':episodes})
  except Exception as ex: 
    return render(request, 'series/show_temporada.html', {'error': ex})

def bcs_season(request, id_season):
  try:
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul')
    lista = response.json()
    episodes = []
    for episode in lista:
        if episode['season'] == str(id_season):
            episodes.append(episode)
    return render(request, 'series/show_temporada.html',{'list':episodes})
  except Exception as ex: 
    return render(request, 'series/show_temporada.html', {'error': ex})

def episode(request, id_episode):
  try:
    link = 'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/'+str(id_episode)
    response = requests.get(link)
    lista = response.json()
    lista[0]['air_date'] = lista[0]['air_date'][0:10]
    return render(request, 'series/show_episode.html',{'list':lista[0]})
  except Exception as ex: 
    return render(request, 'series/show_episode.html', {'error': ex})

def character(request, character):
  try:
    name = character.split(" ")
    if len(name) == 3:
        link1 = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(name[0])+'+'+str(name[1])+'+'+str(name[2])
        link2 = 'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author='+str(name[0])+'+'+str(name[1])+'+'+str(name[2])
    elif len(name) == 2:
        link1 = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(name[0])+'+'+str(name[1])
        link2 = 'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author='+str(name[0])+'+'+str(name[1])
    else:
        link1 = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(name[0])
        link2 = 'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author='+str(name[0])
    response1 = requests.get(link1)
    lista = response1.json()
    response2 = requests.get(link2)
    citas = response2.json()
    return render(request, 'series/show_character.html', {'list':lista[0], 'citas':citas})
  except Exception as ex: 
    return render(request, 'series/show_character.html', {'error': ex})

def search(request):
  try:
    query = request.GET.get('q')
    name = query.split(" ")
    lista = []
    l = []
    i = 0
    if len(name) == 1 and name[0] != '':
      while len(l) > 0 or i == 0:  
        link = 'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(name[0])+'&limit=10&offset='+str(i)
        response = requests.get(link)
        l = response.json()
        lista += l
        if name[0].lower() == 'victor':
            l = []
        i += 10
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
  except Exception as ex: 
    return render(request, 'series/results_search.html', {'error': ex})


