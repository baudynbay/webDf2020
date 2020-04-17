from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import Vacancy, Company
from django.http.response import JsonResponse
from rest_framework.response import Response
from .serializers import CompanySerializer, VacancySerializer, CompanyModelSerializer
import json
from rest_framework.permissions import IsAuthenticated
import rest_framework
from rest_framework.decorators import action
# Create your views here.
@csrf_exempt
def companies(request):
    if request.method == 'GET':
        serializer = CompanyModelSerializer(Company.objects.all(), many=True)
        # serializer = CompanySerializer(Company.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        serializer = CompanyModelSerializer(data=request_body)
        # serializer = CompanySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"data": "error"}, safe=False)
    return JsonResponse("error", safe=False)

@csrf_exempt
def company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        # serializer = CompanySerializer(company)
        serializer = CompanyModelSerializer(company)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse({"error": serializer.errors}, safe=False)
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse('Deleted', safe=False)
    else:
        return JsonResponse("error", safe=False)


def compVacancies(request, id):
    if request.method == 'GET':
        serializer = VacancySerializer(Company.objects.get(id=id).vacancy_set.all(), many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse("error", safe=False)

@csrf_exempt
def vacancies(request):
    if request.method == 'GET':
        serializer = VacancySerializer(Vacancy.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        serializer = VacancySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse({"error": serializer.errors}, safe=False)
    else:
        return JsonResponse("error", safe=False)

@csrf_exempt
def vacancy(request, id):
    try:
        this_vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = VacancySerializer(this_vacancy)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        serializer = VacancySerializer(instance=this_vacancy, data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse({"error": serializer.errors}, safe=False)
    elif request.method == 'DELETE':
        this_vacancy.delete()
        return JsonResponse("Deleted", safe=False)
    else:
        return JsonResponse("error", safe=False)


def vacanciesTopTen(request):
    if request.method == 'GET':
        serializer = VacancySerializer(Vacancy.objects.all().order_by('-salary')[:10], many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse("error", safe=False)

@action(methods=['get'], detail=False)
class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticated,)
    def top_ten(self, request):
        top_ten = self.get_queryset().order_by('-salary')[:10]
        serializer = VacancySerializer(top_ten, many=True)
        return Response(serializer.data)
