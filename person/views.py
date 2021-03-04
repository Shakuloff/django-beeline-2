from random import random

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models.functions import Lower
from django.db.models import Max, Min, Avg, Sum, Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from .models import Person, Country, City
from .filter import detail_filter
# Create your views here.
import json


def index(request):
    contact_list = Person.objects.all().order_by("FirstName")
    total_query = contact_list.count()
    max_salary = contact_list.aggregate(Max('Salary'))
    min_salary = contact_list.aggregate(Min('Salary'))
    avg_salary = contact_list.aggregate(Avg('Salary'))
    print(max_salary)
    countries_list = Country.objects.all().order_by("Name")
    jobs_filter = Person.objects.all().values("Job").distinct()
    paginator = Paginator(contact_list, 10)
    template = loader.get_template('index.html')
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    detail_filters = detail_filter(request.GET, queryset=contact_list)
    print(detail_filters)
    return render(request, 'index.html', {
        'total_query': total_query,
        'max_salary': max_salary,
        'min_salary': min_salary,
        'avg_salary': avg_salary,
        'page_obj': page_obj,
        'countries_list': countries_list,
        'jobs_filter': jobs_filter,
        'filter': detail_filters,
    })


def detail_view(request, person_name):
    person_detail = Person.objects.get(id=person_name)
    contact_list = Person.objects.all().order_by("FirstName")
    countries_list = Country.objects.all().order_by("Name")
    jobs_filter = Person.objects.all().values("Job").distinct()
    detail_filters = detail_filter(request.GET, queryset=contact_list)
    max_salary = contact_list.aggregate(Max('Salary'))
    min_salary = contact_list.aggregate(Min('Salary'))
    avg_salary = contact_list.aggregate(Avg('Salary'))


    print(person_detail)

    return render(request, 'detail_view.html', {
        'max_salary': max_salary,
        'min_salary': min_salary,
        'avg_salary': avg_salary,
        'person': person_detail,
        'countries_list': countries_list,
        'jobs_filter': jobs_filter,
        'filter': detail_filters,
    })


def filter_by_country(request, country_name):
    contact_list_salary = Person.objects.all()
    total_query = contact_list_salary.count()
    contact_list = Person.objects.filter(Countries=country_name)
    max_salary = contact_list_salary.aggregate(Max('Salary'))
    min_salary = contact_list_salary.aggregate(Min('Salary'))
    avg_salary = contact_list_salary.aggregate(Avg('Salary'))
    countries_list = Country.objects.all().order_by("Name")
    jobs_filter = Person.objects.all().values("Job").distinct()
    paginator = Paginator(contact_list, 2)
    template = loader.get_template('index.html')
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {
        'total_query': total_query,
        'max_salary': max_salary,
        'min_salary': min_salary,
        'avg_salary': avg_salary,
        'page_obj': page_obj,
        'countries_list': countries_list,
        'jobs_filter': jobs_filter,
    })


def filter_by_city(request, city_name):
    contact_list_salary = Person.objects.all()
    total_query = contact_list_salary.count()
    contact_list = Person.objects.filter(Cities=city_name)
    max_salary = contact_list_salary.aggregate(Max('Salary'))
    min_salary = contact_list_salary.aggregate(Min('Salary'))
    avg_salary = contact_list_salary.aggregate(Avg('Salary'))
    countries_list = Country.objects.all().order_by("Name")
    jobs_filter = Person.objects.all().values("Job").distinct()
    paginator = Paginator(contact_list, 2)
    template = loader.get_template('index.html')
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {
        'total_query': total_query,
        'max_salary': max_salary,
        'min_salary': min_salary,
        'avg_salary': avg_salary,
        'page_obj': page_obj,
        'countries_list': countries_list,
        'jobs_filter': jobs_filter,
    })


def search(request):
    contact_list = Person.objects.all()
    contact_list_salary = Person.objects.all()
    max_salary = contact_list_salary.aggregate(Max('Salary'))
    min_salary = contact_list_salary.aggregate(Min('Salary'))
    avg_salary = contact_list_salary.aggregate(Avg('Salary'))
    countries_list = Country.objects.all()
    jobs_filter = Person.objects.all().values("Job").distinct()
    detail_filters = detail_filter(request.GET, queryset=contact_list)
    total_query = contact_list_salary.count()
    query = request.GET.get('q')
    a = "".join(query[0].upper()) + query[1:]
    # a = a.lower()
    if query:
        contact_list = Person.objects.filter(
            Q(FirstName__icontains=a) | Q(FamilyName__icontains=a) |
            Q(Patronymic__icontains=a) | Q(PhoneNumber__icontains=a) | Q(PostCode__icontains=a) | Q(Job__icontains=a)
        ).order_by("FirstName").distinct()
        total_query = contact_list.count

    paginator = Paginator(contact_list, 2) # 6 posts per page
    page = request.GET.get('page')
    # page = 2

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'total_query': total_query,
        'max_salary': max_salary,
        'min_salary': min_salary,
        'avg_salary': avg_salary,
        'page_obj': page_obj,
        'countries_list': countries_list,
        'jobs_filter': jobs_filter,
        'filter': detail_filters,
    }
    return render(request, "index.html", context)


def detail_filter_view(request):
    contact_list = Person.objects.all()
    total_query = contact_list.count()
    max_salary = contact_list.aggregate(Max('Salary'))
    min_salary = contact_list.aggregate(Min('Salary'))
    avg_salary = contact_list.aggregate(Avg('Salary'))
    countries_list = Country.objects.all().order_by("Name")
    detail_filters = detail_filter(request.GET, queryset=contact_list)
    jobs_filter = Person.objects.all().values("Job").distinct()
    paginator = Paginator(detail_filters.qs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(detail_filters.qs)
    return render(request, 'filter.html', {
        'total_query': total_query,
        'max_salary': max_salary,
        'min_salary': min_salary,
        'avg_salary': avg_salary,
        'page_obj': page_obj,
        'countries_list': countries_list,
        'jobs_filter': jobs_filter,
        'filter': detail_filters
    })


def chart(request):
    labels = []
    familyname = []
    data = []


    queryset = Person.objects.values('FirstName', 'FamilyName', 'Salary', 'Age').order_by('FirstName')
    sum_age = Person.objects.values_list('FirstName').aggregate(Avg('Age'))
    min_age = Person.objects.values_list('FirstName').aggregate(Min('Age'))
    max_age = Person.objects.values_list('FirstName').aggregate(Max('Age'))
    summary = Person.objects.values_list('FirstName').aggregate(Count('Age'))
    count = Person.objects.values_list('FirstName').aggregate(Count('Age'))
    man = Person.objects.filter(Gender="Мужской")
    woman = Person.objects.filter(Gender="Женский")

    # sex.append(labels, familyname)
    for entry in queryset:
        temp = entry['FirstName'] + ' ' + entry['FamilyName']
        labels.append(temp)
        familyname.append(entry['FamilyName'])
        data.append(entry['Age'])
    # print(sum_salary[0])
    agr_labels = ['Средний возраст', 'Минимальный возраст', 'Максимальный возраст']
    agr = [sum_age['Age__avg'], min_age['Age__min'], max_age['Age__max']]

    sex = ['Количество пользователей', 'Женщины', 'Мужчины']
    sex_num = [count['Age__count'], len(man), len(woman)]
    # print(len(man), len(woman))

    print(sex_num)
    # temp = [{'Всего получили': sum_salary["Salary__max"]}]
    # queryset = Person.objects.values('Salary').order_by('FirstName')
    # for entry in queryset:
    #     # labels.append(entry['FirstName'])
    #     data.append(entry['Salary'])

    # print(temp)
    return JsonResponse(data={
        'labels': labels,
        'familyname': familyname,
        'data': data,
        'agr_labels': agr_labels,
        'agr': agr,
        'sex': sex,
        'sex_num': sex_num,
    })