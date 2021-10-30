import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings

bus_stations = []
name_list = []
street_list = []
district_list = []


class Station:
    def __init__(self, i):
        self.name = name_list[i]
        self.street = street_list[i]
        self.district = district_list[i]


def index(request):
    return redirect(reverse('bus_stations'))


def split_bus_stations():
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        stations_list = list(rows)
    for row in stations_list:
        name_list.append(row[1])
        street_list.append(row[4])
        district_list.append(row[6])
    return name_list, street_list, district_list


def bus_stations_view(request):
    split_bus_stations()

    for i in range(1, len(name_list)):
        bus_stations.append(Station(i))

    page_number = int(request.GET.get('page', 1))
    elements_per_page = 5
    paginator = Paginator(bus_stations, elements_per_page)
    page = paginator.get_page(page_number)
    content = page.object_list

    context = {
        'bus_stations': content,
        'page': page
    }
    return render(request, 'stations/index.html', context)
