from .models import *
from django.http.response import JsonResponse


# Create your views here.


def companies_list(request):
    company_list = Company.objects.all()
    company_json = [company.to_json() for company in company_list]
    return JsonResponse(company_json, safe=False)


def company_get(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
        return JsonResponse(company.to_json())
    except:
        return JsonResponse({'message': 'error'}, status=404)


def company_vacancies(request, company_id):
    # print(Vacancy.company.name)
    try:
        company_name = Company.objects.get(id=company_id)
        vacancies = Vacancy.objects.filter(company=company_name)
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    except:
        return JsonResponse({'message': 'error'}, status=404)


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_get(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
        return JsonResponse(vacancy.to_json())
    except:
        return JsonResponse({'message': 'error'}, status=404)


def vacancy_top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)
