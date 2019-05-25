# coding: utf-8
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def add_edit(request, cls, cform, template, return_url=None, **kwargs):
    pagetitle = kwargs.get('pagetitle', None)
    obj = kwargs.get('obj', None)
    delete = kwargs.get('delete', False)
    if obj:
        obj = get_object_or_404(cls, pk=obj)
    if request.POST:
        if request.POST.has_key('delete'):
            obj.delete()
            return HttpResponseRedirect(reverse(return_url))

        form = cform(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save()
            if return_url:
                return HttpResponseRedirect(reverse(return_url))
            elif obj and hasattr(obj, 'get_absolute_url'):
                return HttpResponseRedirect(obj.get_absolute_url())
    else:
        form = cform(instance=obj)
    return render(request, template, locals())


def list_view(request, cform, template, **kwargs):
    form = cform(request.GET)
    form.is_valid()
    itens = form.query()
    pagetitle = kwargs.get('pagetitle', None)
    add_url = kwargs.get('add_url', None)
    querystring = request.META.get('QUERY_STRING', None)
    return render(request, template, locals())
