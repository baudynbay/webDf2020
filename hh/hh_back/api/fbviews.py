from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Vacancy, Company
from django.http.response import JsonResponse
from .serializers import CompanySerializer, VacancySerializer, CompanyModelSerializer, VacancyModelSerializer
import json
from django.http.response import HttpResponse
from django.http.request import HttpRequest
import rest_framework
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@csrf_exempt
def companies(request):
    if request.method == 'GET':
        serializer = CompanyModelSerializer(Company.objects.all(), many=True)
        # serializer = CompanySerializer(Company.objects.all(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # request_body = json.loads(request.body)
        serializer = CompanyModelSerializer(data=request.data)
        # serializer = CompanySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == 'GET':
        # serializer = CompanySerializer(company)
        serializer = CompanyModelSerializer(company)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # request_body = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"error": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@csrf_exempt
def compVacancies(request, id):
    if request.method == 'GET':
        serializer = VacancyModelSerializer(Company.objects.get(id=id).vacancy_set.all(), many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
@csrf_exempt
def vacancies(request):
    if request.method == 'GET':
        serializer = VacancyModelSerializer(Vacancy.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
        # request_body = json.loads(request.body)
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"error": serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def vacancy(request, id):
    try:
        this_vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return Response({'error': str(e)})
    if request.method == 'GET':
        serializer = VacancyModelSerializer(this_vacancy)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'PUT':
        # request_body = json.loads(request.body)
        serializer = VacancySerializer(instance=this_vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response({"error": serializer.errors})
    elif request.method == 'DELETE':
        this_vacancy.delete()
        return Response("Deleted", status=status.HTTP_202_ACCEPTED)
    else:
        return Response("error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def vacanciesTopTen(request):
    if request.method == 'GET':
        serializer = VacancySerializer(Vacancy.objects.all().order_by('-salary')[:10], many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
