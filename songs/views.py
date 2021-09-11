from typing import NewType
from django.shortcuts import render
from .models import Song,Album

# Create your views here.
def index(request):
    context={
        "songs":Song.objects.all(),     
        "albums":Album.objects.all(),
    }
    return render(request,"songs\index.html",context)

def studioSongs(request):
    alb=Album.objects.filter(Album_title=request.GET["song_album"]).order_by('id').first()
    Song.objects.create(Song_title=request.GET["song_title"],Song_album=alb,Song_Author=request.GET["song_author"])
    context={
        "songs":Song.objects.all(),
        "albums":Album.objects.all(),
        "recent":request,
    }
    return render(request,"songs\studioDatas.html",context)

def studioDeleteSongs(request):
    song=Song.objects.filter(Song_title=request.GET["song_title"]).order_by('id').first()
    song.delete()
    context={
        "songs":Song.objects.all(),
        "albums":Album.objects.all(),
        "recent":request,
    }
    return render(request,"songs\studioDatas.html",context)

def studioDeleteAlbums(request):
    album=Album.objects.filter(Album_title=request.GET["album_title"]).order_by('id').first()
    album.delete()
    context={
        "songs":Song.objects.all(),
        "albums":Album.objects.all(),
        "recent":request,
    }
    return render(request,"songs\studioDatas.html",context)

def studioAlbums(request):
    Album.objects.create(Album_title=request.GET["album_title"],Album_format=request.GET["album_format"],CopyRight_Date=request.GET["album_cpyD"])
    context={
        "songs":Song.objects.all(),
        "albums":Album.objects.all(),
    }
    return render(request,"songs\studioDatas.html",context)

def studio(request):
    context={
        "songs":Song.objects.all(),
        "albums":Album.objects.all(),
    }
    return render(request,"songs\studioDatas.html",context)