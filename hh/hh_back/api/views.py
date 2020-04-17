from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Vacancy, Company
from django.http.response import JsonResponse
from rest_framework.response import Response
from .serializers import CompanySerializer, VacancySerializer
import json
import rest_framework

# Create your views here.
@csrf_exempt
def companies(request):
    if request.method == 'GET':
        serializer = CompanySerializer(Company.objects.all(), many=True)
        # json_comps = [c.to_json() for c in Company.objects.all()]
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':

        # data = json.loads(request.body)
        # comp = Company.objects.create(name=data['name'], city=data['city'], description=data['description'], address=data['address'])
        # return JsonResponse(comp.to_json())
        serializer = CompanySerializer(data=request.body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse("invalid", safe=False)
            return JsonResponse({"data": "error"}, safe=False)
    return JsonResponse("error", safe=False)

@csrf_exempt
def company(request, id):
    try:
        category = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        return JsonResponse(category.to_json(), safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        category.name = data.get('city', category.name)
        category.city = data.get('city', category.city)
        category.description = data.get('description', category.description)
        category.address = data.get('address', category.address)
        category.save()
        return JsonResponse(category.to_json(), safe=False)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse('Deleted', safe=False)
    else:
        return JsonResponse("error", safe=False)


def compVacancies(request, id):
    if request.method == 'GET':
        vacancies1 = Company.objects.get(id=id).vacancy_set.all()
        json_vacs = [v.to_json() for v in Company.objects.get(id=id).vacancy_set.all()]
        return JsonResponse(json_vacs, safe=False)
    else:
        return JsonResponse("error", safe=False)


def vacancies(request):
    if request.method == 'GET':
        json_vacs = [v.to_json() for v in Vacancy.objects.all()]
        return JsonResponse(json_vacs, safe=False)
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        return JsonResponse("error", safe=False)
    else:
        return JsonResponse("error", safe=False)


def vacancy(request, id2):
    try:
        this_vacancy = Vacancy.objects.get(id=id2)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
    elif request.method == 'DELETE':
        this_vacancy.delete()
    else:
        return JsonResponse("error", safe=False)


def vacanciesTopTen(request):
    if request.method == 'GET':
        json_vacs = [v.to_json() for v in Vacancy.objects.all().order_by('-salary')[:10]]
        return JsonResponse(json_vacs, safe=False)
    else:
        return JsonResponse("error", safe=False)
