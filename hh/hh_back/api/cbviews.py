from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Vacancy, Company
from django.http.response import JsonResponse
from rest_framework.response import Response
from .serializers import CompanySerializer, VacancySerializer, CompanyModelSerializer
import json
import rest_framework
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
class CompanyListView(APIView):

    def get(self, request):
        companies = Company.objects.all()
        ser = CompanySerializer(companies, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = CompanySerializer(request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CompanyDetailView(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})
    def get(self, request, id):
        company = self.get_object(id)
        ser = CompanySerializer(company)
        return Response(ser.data)
    def put(self, request, id):
        serializer = CompanySerializer(instance=self.get_object(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error": serializer.errors})
    def delete(self, request, id):
        company = self.get_object(id)
        company.delete()
        return Response({"Deleted": True})

