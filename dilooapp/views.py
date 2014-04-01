from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect


from dilooapp.models import Category, Thing, Review

# Create your views here.

def home(request):
	context = RequestContext(request)
	categories = Category.objects.all()
	things = Thing.objects.all().order_by('-dateCreated')
	reviews = Review.objects.all()
	return render_to_response("index.html", {'categories': categories, 'things': things, 'reviews': reviews, 'user': request.user}, context)


def category(request, id_category):
	categories = Category.objects.all()
	things = Thing.objects.filter(category=id_category)
	return render_to_response("index.html", {'categories': categories, 'things': things, 'user': request.user}) 

def index(request):
	context = RequestContext(request)
	return render_to_response("login_page.html", {'hola': 'mundo', 'username': request.user}, context)

def login(request):
	context = RequestContext(request)
	exists = True
	paso = 'No ha pasado: ' + request.user.username
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				exists = True
				paso = 'paso: ' + request.user.username
			else:
				pass	
		else: 
			pass
	else:
		pass
	return render_to_response("login_page.html", {'ya':paso, 'exist': exists, 'user': user}, context)

def show(request, numero):
	return HttpResponse("Tu numero es:" +numero)

def logout(request):
	context = RequestContext(request)
	auth_logout(request)
	return HttpResponseRedirect('/login/')


