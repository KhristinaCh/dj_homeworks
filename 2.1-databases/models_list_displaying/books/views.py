from django.shortcuts import render
from django.core.paginator import Paginator

import re

from .models import Book


def books_view(request, date=None):
    # date = request.GET.get('date', None)

    template = 'books/books_list.html'
    books_query = Book.objects.all()
    dates = []
    data = Book.objects.values()
    for i in data:
        dates.append(str(i['pub_date']))
    dates.sort()
    if date:
        books = Book.objects.filter(pub_date=date)
        if date == dates[0]:
            date1 = None
            date2 = dates[1]
        elif date == dates[len(dates)-1]:
            date1 = dates[dates.index(date) - 1]
            date2 = None
        else:
            date1 = dates[dates.index(date) - 1]
            date2 = dates[dates.index(date) + 1]
    else:
        books = books_query
        date1 = None
        date2 = None
    context = {
        'books': books,
        'previous_page': date1,
        'next_page': date2
    }
    return render(request, template, context)

