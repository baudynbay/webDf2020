from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token
from api.views_fbv import company_vacancies
from api.views_generic import CompanyListAPIView, CompanyDetailAPIView, VacancyListAPIView, VacancyDetailAPIView

# urlpatterns = [
#     path('login/', obtain_jwt_token),
#     path('vacancies/', vacancy_list),
#     path('vacancies/<int:vacancy_id>/', vacancy_detail),
#     path('companies/', company_list),
#     path('companies/<int:company_id>/', company_detail),
#     path('companies/<int:pk>/vacancies/', company_vacancies),
#     # path('vacancies/top_ten/', top_ten_vacancies)
# ]

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/', VacancyDetailAPIView.as_view()),
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:pk>/vacancies/', company_vacancies),
    # path('vacancies/top_ten/', top_ten_vacancies)
]