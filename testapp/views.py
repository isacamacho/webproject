from datetime import datetime
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def suma(request, a, b):
    response = {'resultado': int(a) + int(b)


     }
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def suma_post(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})




def gallery(request):
    return render(request, 'testapp/gallery.html')

from django.shortcuts import render

def gallery_photo(request, photo):
    context = {'photo': photo}
    return render(request, 'testapp/gallery_photo.html', context)