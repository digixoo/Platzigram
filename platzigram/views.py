#Django
from django.http import HttpResponse
from django.http.response import JsonResponse

def sorted_integers(request) -> HttpResponse:
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    numbers = sorted(numbers)

    data = {
        'status': 'OK',
        'data': numbers
    }
    
    return JsonResponse(data, safe=False)

def say_hi(request, name, age) -> HttpResponse:
    if age < 12:
        message = f'Lo lamentamos {name} pero no cumple con la edad permitida'
    else:
        message = f'hola {name}!, bienvenido a Platzigram'
    
    return HttpResponse(message)