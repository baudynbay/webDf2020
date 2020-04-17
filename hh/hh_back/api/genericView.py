from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Company, Vacancy

from .serializers import CompanySerializer, VacancySerializer, CompanyModelSerializer


class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)


class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # permission_classes = (IsAuthenticated,)


class VacancyListAPIView(generics.ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    # permission_classes = (IsAuthenticated,)


class VacancyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    # permission_classes = (IsAuthenticated,)