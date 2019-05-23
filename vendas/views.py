from django.shortcuts import render,redirect
from django.contrib.auth import logout as django_logout
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import json

# Create your views here.

def home(request):
    return render(request,'vendas/home.html')


def my_logout(request):
    logout(request)
    return redirect('home')

def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def user_json_lookup(request):
    # q = request.GET.get('q', '')
    # users = [u.get_json for u in User.objects.filter(Q(first_name__icontains=q) |Q(last_name__icontains=q) | Q(username__icontains=q) | Q(email__icontains=q)).order_by('first_name')]
    users = [u.get_json() for u in User.objects.all()]
    return HttpResponse(json.dumps(users), content_type='application/json')

def mylogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,'vendas/home.html')       