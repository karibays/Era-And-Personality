from django.shortcuts import render
from main.models import Person


def index(request):
    person = Person.objects.all()
    context = {
        'persons': person
    }

    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def work(request):
    person = Person.objects.all()
    context = {
        'persons': person
    }
    return render(request, 'main/portfolio.html', context)



# {% load static %}
# <!doctype html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport"
#           content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <title>Document</title>
#     <link rel="stylesheet" href="{% static 'main/css/style.css'%}">
# </head>
# <body>
# HELLO WORLD
# </body>
# </html>