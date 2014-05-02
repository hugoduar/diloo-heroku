from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from app.models import Category, Review, Critic
from app.forms import UserForm, CriticForm

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.


# Pagina de inicio
# Vista principal

def main(request):
    user_form = UserForm(data=request.POST)
    critic_form = CriticForm(data=request.POST)
    if request.user.is_active:
        return HttpResponseRedirect('/feed')
    else:
        reviews = Review.objects.all()
        return render_to_response("index.html", {"reviews": reviews, "user_form":user_form, "critic_form":critic_form}, RequestContext(request)) 

@login_required(login_url='/')	
def feed(request):
    context = RequestContext(request)
    categories = Category.objects.all()
    reviews = Review.objects.all()
    personal_reviews = Review.objects.all()
    if request.user.is_active:
    	critic = Critic.objects.get(id=1)
    	personal_reviews = Review.objects.all()
    return render_to_response("feed.html", {'categories': categories, 'reviews': reviews, 'user': request.user, 'personal_reviews': personal_reviews}, context)


def login(request):
    context = RequestContext(request)
    user = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                pass
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    elif request.method == 'GET' and user is None: 
		return HttpResponseRedirect('/')
    else:
    	return render_to_response("login_page.html", {}, context)


def logout(request):
    context = RequestContext(request)
    auth_logout(request)
    return HttpResponseRedirect('/')

def register(request):
    context = RequestContext(request)
    if request.method == 'POST':
    	form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
        return HttpResponseRedirect('/')




