# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from models import Gracz
from main.forms import FormularzLogowania, FormularzRejestracji

def index(request):
    user = request.user
    if user.is_active and user.username!='pmanager':
        gracz = Gracz.objects.get(nazwa=user.username)

    # return render(request, 'index.html')
    return render_to_response('index.html', locals())

def player_list(request):

    user = request.user

    gracz = Gracz.objects.get(nazwa=user.username)

    players = User.objects.all()
    liczba = User.objects.count()
    liczba -= 1
    return render_to_response('players.html', locals())

def register_page(request):
    if request.method == 'POST':
        form = FormularzRejestracji(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
              username=form.cleaned_data['username'],
              password=form.cleaned_data['password1'],
              email=form.cleaned_data['email']
            )
            user.save()
            temp_rasa = form.cleaned_data['rasa']
            temp_nazwa_grodu = form.cleaned_data['nazwa_grodu']
            if temp_rasa=="czlowiek":
                temp_power = 80
                temp_gold = 1000
                b = Gracz(user=user, rasa=temp_rasa, power=temp_power, gold=temp_gold, nazwa=form.cleaned_data['username'], uniwersytet = True, nazwa_grodu = temp_nazwa_grodu)
                b.save()
            elif temp_rasa=="goblin":
                temp_power = 120
                temp_gold = 500
                b = Gracz(user=user, rasa=temp_rasa, power=temp_power, gold=temp_gold, nazwa=form.cleaned_data['username'], prorok = True, nazwa_grodu = temp_nazwa_grodu)
                b.save()


            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request, user)

            # template = get_template("registration/register_success.html")
            # variables = RequestContext(request,{'username':form.cleaned_data['username']})
            # output = template.render(variables)
            # return HttpResponse(output)
            # return HttpResponseRedirect("/")

            template = get_template("index.html")
            variables = RequestContext(request,{'user':user})
            output = template.render(variables)
            return  HttpResponseRedirect("/")

            # template = get_template("tworzenie.html")
            # variables = RequestContext(request,{'user':user})
            # output = template.render(variables)
            # return  HttpResponse(output)

    else:
        form = FormularzRejestracji()
    template = get_template("registration/register.html")
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)

def login_page(request):
    if request.method == 'POST':
        form = FormularzLogowania(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            login(request,user)
            template = get_template("index.html")
            variables = RequestContext(request,{'user':user})
            output = template.render(variables)
            return HttpResponseRedirect("/")
    else:
        form = FormularzLogowania()
    template = get_template("login.html")
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")


def panel(request):

    user = request.user

    gracz = Gracz.objects.get(nazwa=user.username)

    return render_to_response('panel.html', locals())


def widok_miasta(request):

    user = request.user

    gracz = Gracz.objects.get(nazwa=user.username)

    return render_to_response('widok_miasta.html', locals())


def uniwersytet(request):

    user = request.user

    gracz = Gracz.objects.get(nazwa=user.username)

    return render_to_response('uniwersytet.html', locals())


def prorok(request):

    user = request.user

    gracz = Gracz.objects.get(nazwa=user.username)

    return render_to_response('prorok.html', locals())


def koszary_ludzi(request):

    user = request.user

    gracz = Gracz.objects.get(nazwa=user.username)

    return render_to_response('koszary_ludzi.html', locals())

def koszary_goblinow(request):

    user = request.user

    gracz = Gracz.objects.get(nazwa=user.username)

    return render_to_response('koszary_goblinow.html', locals())