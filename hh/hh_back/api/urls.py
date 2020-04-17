from django.urls import path

from . import view_old, views, fbviews
from .cbviews import CompanyDetailView
from .genericView import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView, VacancyDetailAPIView
urlpatterns = [
    # path('companies', CompanyListAPIView.as_view()),
    # path('companies/<int:id>', CompanyDetailAPIView.as_view()),
    # path('companies/<int:id>/vacancies', fbviews.compVacancies),
    # path('vacancies', VacancyListAPIView.as_view()),
    path('vacancies/<int:id>', fbviews.vacancy),
    # path('vacancies/top_ten', view_old.VacancyViewSet),
    # path('companies/class', views),

    path('companies', CompanyListAPIView.as_view()),
    path('companies/<int:pk>', CompanyDetailAPIView.as_view()),
    path('companies/<int:id>/vacancies', fbviews.compVacancies),
    path('vacancies', fbviews.vacancies),
    # path('vacancies/<int:pk>', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten', view_old.vacanciesTopTen),
    # path('companies/class', views),
]