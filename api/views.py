import requests, hashlib, json, time
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings


def index(request):
    return render_to_response('template.html')


def personajes(request, offset_id=0):
    return peticion({'offset': offset_id}, 'characters')


def personajeID(request, personaje_id):
    return peticion({}, 'characters/'+personaje_id)


def comics(request, offset_id=0):
    return peticion({'offset': offset_id}, 'comics')


def comicID(request, comic_id):
    return peticion({}, 'comics/'+comic_id)


def creadores(request, offset_id=0):
    return peticion({'offset': offset_id}, 'creators')


def creadorID(request, creador_id):
    return peticion({}, 'creators/'+creador_id)


def peticion(params=None, url=None):
    ts = int(time.time())
    m = hashlib.md5()
    m.update(str(ts)+settings.PRIVATE_KEY+settings.PUBLIC_KEY)
    payload = {'ts': ts, 'apikey': settings.PUBLIC_KEY, 'hash': m.hexdigest()}
    payload.update(params)
    r = requests.get(settings.URL_API+url, params=payload)
    data = json.dumps(r.json())
    response = HttpResponse(data, mimetype='application/json')
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response