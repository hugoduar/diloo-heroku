from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect


from dilooapp.models import Category, Thing, Review
from dilooapp.forms import UserForm
# Create your views here.


def base(request):
    user = request.user
    return render_to_response("base.html", {'user': user})


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
    


def show(request, numero):
    n = request.GET['p']
    return HttpResponse("Tu numero es:" + numero + n)


def logout(request):
    context = RequestContext(request)
    auth_logout(request)
    return HttpResponseRedirect('/')


def register(request):
	context = RequestContext(request)
    if request.method == 'POST':
    	form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()

    return render_to_response("registrar.html", {'form': form}, context)
