from django.shortcuts import render,redirect
from django.contrib.auth import logout as django_logout
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
import json 
from tablib import Dataset
from .forms import PersonForm,FormQueryClassificacao,FormClassificacao
from .models import Person,Classificacao
from django.shortcuts import get_list_or_404, get_object_or_404
from django.forms import modelformset_factory
# from vendas.tables import PersonTable
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from admin.contrib.generic_view import add_edit, list_view
from django.utils.translation import ugettext_lazy as _
from .forms import PostForm
from .models import Post,UsuarioWeb


def home(request):
    return render(request,'vendas/home.html')


def my_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
#     return redirect('home')

def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('home'))

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


def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')


@login_required
def persons_list(request):
    persons = PersonTable()
    return render(request, 'vendas/person.html',{'persons':persons})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'vendas/person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'vendas/person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'vendas/person_delete_confirm.html', {'person': person})


@login_required
def edit_classificao(request, obj=None, template='vendas/classificacao.html'):
        return add_edit(request, Classificacao, FormClassificacao, template, 'fiscal_classificacao', obj=obj, pagetitle=_(u'Classificação Fiscal'))


@login_required
def classificacao(request, template='vendas/classificacoes.html'):
    return list_view(request, FormQueryClassificacao, template, pagetitle=_(u'Classificação Fiscal'), add_url='edit_classificacao')

#home view for posts. Posts are displayed in a list

class IndexView(ListView):
 template_name='vendas/list.html'
 context_object_name = 'post_list'
 def get_queryset(self):
  return Post.objects.all()

#Detail view (view post detail)
class PostDetailView(DetailView):
 model=Post
 template_name = 'vendas/post-detail.html'

#New post view (Create new post)
def postview(request):
 if request.method == 'POST':
  form = PostForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('index')
 form = PostForm()
 return render(request,'vendas/post.html',{'form': form})

#Edit a post
def edit(request, pk, template_name='vendas/edit.html'):
    post= get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

#Delete post
def delete(request, pk, template_name='vendas/confirm_delete.html'):
    post= get_object_or_404(Post, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object':post})



class UserView(ListView):
 template_name='vendas/userlist.html'
 context_object_name = 'user_list'
 def get_queryset(self):
  return UsuarioWeb.objects.all()