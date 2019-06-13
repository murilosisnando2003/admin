from django.shortcuts import render
from .models import view_alertaremanufatura
from admin.contrib.generic_view import add_edit, list_view
from django.views.generic import ListView, DetailView
from .forms import RemanufaturaForm
from django.shortcuts import get_object_or_404,redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


class RemanufaturaView(ListView):
 template_name='vendas/remanufatura.html'
 context_object_name = 'remanufatura_list'
 def get_queryset(self):
  return view_alertaremanufatura.objects.all()


#Edit a post
def edit(request, pk, template_name='vendas/edit-remanufatura.html'):
    edit= get_object_or_404(view_alertaremanufatura, pk=pk)
    form = RemanufaturaForm(request.POST or None, instance=edit)
    if form.is_valid():
        # form.save()
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['murilorodrigues@edgeglobalsupply.com.br',]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('remanufatura')
    return render(request, template_name, {'form':form})

