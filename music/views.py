__author__ = 'anuraagbasu'

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.db.models import Q

from music.models import Track, Genre

def index (request):
    trackList = Track.objects.order_by('createDate')[:10]
    genreList = Genre.objects.all()[:10]
    context = dict()
    context['trackList'] = trackList
    context['genreList'] = genreList
    return render(request, "music/index.html", context)

def showAllTracks (request):
    searchText = request.GET.get('search')
    if searchText!="":
        tracksList = Track.objects.filter(title__icontains=searchText)
    else:
        tracksList = Track.objects.order_by('createDate')
    context = dict()
    context['tracksList'] = tracksList
    context['maxRating'] = range(1, 6)
    context['searchText'] = searchText
    return render(request, "music/track.list.html", context)

def addTrack (request):
    if request.method == "POST":
        trackTitle = request.POST.get('title')
        if trackTitle!="":
            try:
                track = Track(title=trackTitle, rating=request.POST.get('rating'), )
                track.save()
                genres = request.POST.getlist('genres')
                for genreId in genres:
                    genre = Genre.objects.get(pk=genreId)
                    track.genres.add(genre)
            except ():
                return render(request, 'music/track.add.html', {
                    'error_message': "Something aweful happened. Try again"
                })
            else:
                return HttpResponseRedirect(reverse('music:showAllTracks'))
        else:
            return render(request, 'music/track.add.html', {
                'error_message': "Can't save empty Track"
            })
    else:
        genreList = Genre.objects.all()
        context = dict()
        context['genreList'] = genreList
        return render(request, 'music/track.add.html', context)

def trackDetail (request, trackId):
    track = get_object_or_404(Track, pk=trackId)
    context = dict()
    context['track'] = track
    return render(request, "music/track.show.html", context)

def trackUpdate (request, trackId):
    if request.method == "POST":
        trackTitle = request.POST.get('title')
        if trackTitle!="":
            trackRating = request.POST.get('rating')
            try:
                Track.objects.filter(pk=trackId).update(title=trackTitle, rating=trackRating)
                track = Track.objects.get(pk=trackId)
                track.genres.clear()
                genres = request.POST.getlist('genres')
                for genreId in genres:
                    genre = Genre.objects.get(pk=genreId)
                    track.genres.add(genre)
            except () :
                return render(request, 'music/track.edit.html', {
                    'error_message': "Something aweful happened. Try again"
                })
            else:
                return HttpResponseRedirect(reverse('music:showAllTracks'))
        else:
            return render(request, 'music/track.add.html', {
                'error_message': "Can't save empty Track"
            })
    else:
        track = Track.objects.get(pk=trackId)
        genreList = Genre.objects.all()
        context = dict()
        context['track'] = track
        context['genreList'] = genreList
        return render(request, "music/track.edit.html", context)

def showAllGenres (request):
    searchText = request.GET.get('search')
    if searchText!="":
        genreList = Genre.objects.filter(name__icontains=searchText)
    else:
        genreList = Genre.objects.all()
    context = dict()
    context['genreList'] = genreList
    context['searchText'] = searchText
    return render(request, "music/genre.list.html", context)

def addGenre (request):
    if request.method == "POST":
        genreName = request.POST.get('name')
        if genreName!="":
            try:
                genre = Genre(name=genreName, description=request.POST.get('description'))
                genre.save()
            except ():
                return render(request, 'music/genre.add.html', {
                    'error_message': "Something aweful happened"
                })
            else:
                return HttpResponseRedirect(reverse('music:showAllGenres'))
        else:
            return render(request, 'music/genre.add.html', {
                'error_message': "Can't save empty Genre"
            })
    else:
        return render(request, 'music/genre.add.html')

def genreDetail (request, genreId):
    genre = get_object_or_404(Genre, pk=genreId)
    context = dict()
    context['genre'] = genre
    return render(request, "music/genre.show.html", context)

def genreUpdate (request, genreId):
    if request.method == "POST":
        genreName = request.POST.get('name')
        if genreName!="":
            genreDescription = request.POST.get('description')
            try:
                Genre.objects.filter(pk=genreId).update(name=genreName, description=genreDescription)
            except ():
                return render(request, 'music/genre.edit.html', {
                    'error_message': "Something aweful happened. Try again"
                })
            else:
                return HttpResponseRedirect(reverse('music:showAllGenres'))
        else:
            return render(request, 'music/genre.edit.html', {
                'error_message': "Can't save empty Genre"
            })
    else:
        genre = Genre.objects.get(pk=genreId)
        context = dict()
        context['genre'] = genre
        return render(request, 'music/genre.edit.html', context)