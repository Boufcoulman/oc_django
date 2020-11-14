# from django.shortcuts import render
from django.http import HttpResponse
from .models import ALBUMS


def index(request):
    message = "Cc la mif !"
    return HttpResponse(message)


def listing(request):
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = """<ul>{}</ul>""".format("\n".join(albums))
    return HttpResponse(message)


def detail(request, album_id):
    id = int(album_id)  # make sure we have an integer.
    album = ALBUMS[id]  # get the album with its id.
    artists = ", ".join([artist['name'] for artist in album['artists'][:-1]]) + " et " + album['artists'][-1]['name'] if len(album['artists']) > 1 else album['artists'][0]['name']
    message = f"Le nom de l'album est {album['name']}. Il a été écrit par {artists}."
    return HttpResponse(message)


def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Aucun artiste n'est demandé"
    else:
        albums = [
            album for album in ALBUMS
            if query in " ".join(artist['name'] for artist in album['artists'])
        ]

        if len(albums) == 0:
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            albums = ["<li>{}</li>".format(album['name']) for album in albums]
            message = """
                Nous avons trouvé les albums correspondant à votre requête ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(albums))

    return HttpResponse(message)
