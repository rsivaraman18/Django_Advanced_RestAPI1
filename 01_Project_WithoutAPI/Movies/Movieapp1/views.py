from django.shortcuts import render
from django.shortcuts import HttpResponse
from Movieapp1.models import *
from django.http import JsonResponse,HttpResponseBadRequest
import json
from django.views.decorators.csrf import csrf_exempt

def movie_list(request):
    movies_query         = MyMovie.objects.all()     ### Queryset
    movies_query_values  = movies_query.values()     ### Queryset
    movieslistofquery    = list(movies_query_values)  ###Queryset inside a list
    moviesdictofdict     = {'movies':movieslistofquery} ## Dictionary
    # JSONResponse Converts only PythonDict to JSON
    return JsonResponse(moviesdictofdict) 


def movie_listbyid(request,id):
    movie = MyMovie.objects.get(id=id)
    data = {'movie'      :movie.name,'description':movie.description,'active':movie.active}
    return JsonResponse(data)


@csrf_exempt
def movies_create(request):
    if request.method == 'POST':
        try:
            user_request = request.body
            data = json.loads(user_request)

            name        = data.get('name')
            description = data.get('description')
            active      = data.get('active', True)
            
            if not name or not description:
                return HttpResponseBadRequest('Name and description are required.')
                
            movie = MyMovie.objects.create(name=name, description=description, active=active)
            return JsonResponse({'id': movie.id, 'name': movie.name, 'description': movie.description, 'active': movie.active})
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON data.')
    return HttpResponseBadRequest('Only POST method is allowed.')


def movie_update(request, id):
    if request.method == 'PUT':
        try:
            movie =MyMovie.objects.get(id)
            data = json.loads(request.body)
            
            name        = data.get('name')
            description = data.get('description')
            active      = data.get('active')
            
            if name is not None:
                movie.name = name
            if description is not None:
                movie.description = description
            if active is not None:
                movie.active = active
                
            movie.save()
            return JsonResponse({'id': movie.id, 'name': movie.name, 'description': movie.description, 'active': movie.active})
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON data.')
    return HttpResponseBadRequest('Only PUT method is allowed.')