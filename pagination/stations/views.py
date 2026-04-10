from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from pagination.settings import BUS_STATION_CSV
from django.urls import reverse
import csv


class Tramballor():
    """
    Нужен для нормального обращения к предполагаемому 'списку' в html-шаблоне
    От куда методы или поля :/
    """
    def __init__(self, dict_csv):
        self.Name = dict_csv['Name']
        self.Street = dict_csv['Street']
        self.District = dict_csv['District']


with open(BUS_STATION_CSV, encoding="utf-8") as fl:
    data_csv = list(csv.DictReader(fl))
    padin = Paginator(data_csv, 15)


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    q_params_url = request.GET.get('page', 1)

    current_page = padin.get_page(q_params_url)

    list_bus_stations = []

    for i in current_page.object_list:
        list_bus_stations.append(Tramballor(i))

    context = {
        'bus_stations': list_bus_stations,
        'page': current_page,
        'index_Name': 1,
        'index_Street': 4,
        'index_District': 6,

    }
    return render(request, 'stations/index.html', context)



