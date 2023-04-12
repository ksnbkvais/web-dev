from .views import *
from django.urls import path

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:company_id>/', company_get),
    path('companies/<int:company_id>/vacancies/', company_vacancies),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_get),
    path('vacancies/top_ten/', vacancy_top_ten),
]