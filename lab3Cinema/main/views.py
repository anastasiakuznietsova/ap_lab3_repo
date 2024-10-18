from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

import json
from django.http import JsonResponse

from .models import Viewer,Ticket,MovieSession,Showtime
from .forms import ViewerForm, TicketForm,MovieSessionForm
from main.repositories.all_repos import ShowtimeRepo,MovieRepo
#from main.repositories.all_repos import allRepos
from .repositories.models_repo import TicketMovieSessionRepo,ViewerRepo


def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('showtime')

    if request.method=='POST':
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=phone_number)
        except:
            messages.error(request,'User does not exist')
        user=authenticate(request,username=phone_number,password=password)
        if user is not None:
            login(request,user)
            return redirect('showtime')
        else:
            messages.error(request,'Invalid username or password')

    context = {'page':page}
    return render(request,'main/login_register.html',context)

def logoutPage(request):
    logout(request)
    return redirect('showtime')

def registerPage(request):
    form=UserCreationForm()
    viewerform=ViewerForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        viewerform = ViewerForm(request.POST)
        if form.is_valid() and viewerform.is_valid():
            form.save()
            viewerform.save()
            return redirect('login')
        else:
            messages.error(request,'An error occurred during registration')
    context={'form':form,
             'viewerform':viewerform}
    return render(request,'main/login_register.html',context)

def JSONresponse(request):
    if request.method == 'GET':
        showtime=Showtime.objects.get(id=1)
    context={
        'Title':showtime.movie.title,
        'Price':showtime.price,
        'Date':showtime.show_date
    }
    return JsonResponse(context)

def showtime(request):
    q=request.GET.get('q') if request.GET.get('q') else ''
    repo = ShowtimeRepo()
    showtime=repo.get_showtime_by_movie_title(q)
    movie_names = repo.get_all_movie_names()

    showtime_count=showtime.count()
    context={'showtime':showtime,
             'movie_names':movie_names,
             'showtime_count':showtime_count}
    return render(request,'showtime.html',context)

@login_required(login_url='login')
def bookATicket(request):
    viewer = Viewer.objects.get(id=request.user.id)
    ticket_form, moviesession_form = TicketForm(), MovieSessionForm()
    if request.method == 'POST':
        repo = TicketMovieSessionRepo()
        ticket_form, moviesession_form = repo.bookingTicket(request.POST,request.POST,viewer)

        if ticket_form and moviesession_form:
            return redirect('showtime')
    context = {'ticket_form': ticket_form,
               'moviesession_form': moviesession_form}
    return render(request, 'main/bookATicket.html', context)

def movie_information(request,title):
    movie_id=MovieRepo()
    movie = MovieRepo().getById(movie_id.getByTitle(title))
    context={'movie':movie}
    return render(request, 'movie_information.html', context)

@login_required(login_url='login')
def viewer_information(request):
    phone_number = request.user.username
    repoTicket = TicketMovieSessionRepo()
    viewer = Viewer.objects.filter(phone_number=phone_number).first()
    if viewer is None:
        messages.error(request, "Viewer not found.")
        return redirect('showtime')
    ticket_movie_info = repoTicket.getTicketWithSession(viewer)
    context = {
        'viewer': viewer,
        'ticket_movie_info': ticket_movie_info,
    }
    return render(request, 'main/viewer_info.html', context)

def updateTicket(request, id):
    viewer = Viewer.objects.get(id=request.user.id)
    repo = TicketMovieSessionRepo()
    ticket = Ticket.objects.get(id=id)
    session = MovieSession.objects.get(id=id)
    if request.method == 'POST':
        ticket_form, session_form = repo.updateTicket(id, request.POST, request.POST)
        if ticket_form and session_form:
            return redirect('accounts-information')
    else:
        ticket_form = TicketForm(instance=ticket)
        session_form = MovieSessionForm(instance=session)
    context={
        'ticket_form': ticket_form,
        'moviesession_form': session_form,
        'ticket_id': id,
    }
    return render(request, 'main/updateTicket.html', context)

def ticketCancellation(request, id):
    if request.method == 'POST':
        repo = TicketMovieSessionRepo()
        repo.deleteObj(id)
        return redirect('showtime')
    return render(request, 'main/delete.html')