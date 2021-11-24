from django.http.response import JsonResponse, HttpResponse
from django.template import loader


def create_user(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'user created'})
    else:
        return HttpResponse('ERROR 400', status=400)


def list_users(request):
    if request.method == 'GET':
        return JsonResponse({'1': 'user_1',
                             '2': 'user_2'})
    else:
        return HttpResponse('ERROR 400', status=400)


def user_details(request):
    if request.method == 'GET':
        return JsonResponse({'id': '1',
                             'datetime': '21.11.2021 20:30',
                             'name': 'user_1'})
    else:
        return HttpResponse('ERROR 400', status=400)


def users(request):
    template = loader.get_template('11.html')
    return HttpResponse(template.render())
