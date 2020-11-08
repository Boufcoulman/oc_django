# from django.shortcuts import render
from django.http import HttpResponse
from .models import ALBUMS


def index(request):
    message = "Cc la mif !"
    return HttpResponse(message)


def listing(request):
    albums = ["<li>{}</li>".format(album['artists'][0]['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)
