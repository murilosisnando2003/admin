import re
import unicodedata
import datetime
import os
from django.template.defaultfilters import slugify
from django.conf import settings
from django.core.files.storage import default_storage
from django.conf import settings
import uuid

def only_number(value):
    return re.sub("[^\d]+", "", value)


def not_combining(char):
    return unicodedata.category(char) != 'Mn'

def strip_accents(text, encoding=None):
    if encoding is None:
        encoding='utf-8'
    if isinstance(text, unicode):
        unicode_text = unicodedata.normalize('NFD', text)
    else:
        unicode_text = unicodedata.normalize('NFD', text.decode(encoding))
    return filter(not_combining, unicode_text).encode(encoding)

class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''

    def decrement(self):
        self.count -= 1
        return ''

    def double(self):
        self.count *= 2
        return ''


class cached_property(object):
    def __init__(self, func):
        self.__doc__ = getattr(func, '__doc__')
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value


def sender_pre_save(signal, instance, sender, **kwargs):
    update_slug(instance, sender)


def update_slug(instance, sender):
    if not instance.slug:
        if hasattr(instance, 'get_field_for_slug'):
            slug = slugify(instance.get_field_for_slug())
        else:
            slug = slugify(instance)
        novo_slug = slug
        contador = 0
        while sender.objects.filter(slug=novo_slug).exclude(id=instance.id).count() > 0:
            contador += 1
            novo_slug = '%s-%d'%(slug, contador)
        instance.slug = novo_slug.lower()


def get_temporary_report_name(name):
    if settings.DEBUG:
        name, ext = os.path.splitext(name)
        name = '%s-%s%s' % (slugify(name),datetime.datetime.now().strftime("%Y%m%d%H%M%S"), ext)
        path_receiver = ['receiver', 'reports', str(uuid.uuid4())]
        _file_path = os.path.join(settings.MEDIA_ROOT, *path_receiver)
        if not os.path.exists(_file_path):
            os.mkdir(_file_path)

        _file_path =  os.path.join(_file_path, name)

        url = settings.MEDIA_URL + '/'.join(path_receiver) + '/' + name
        return _file_path, url
    else:
        name, ext = os.path.splitext(name)
        name = '%s-%s%s' % (slugify(name),datetime.datetime.now().strftime("%Y%m%d%H%M%S"), ext)
        path_receiver = ['receiver', 'reports', str(uuid.uuid4())]
        _file_path = os.path.join(*path_receiver)
        if not default_storage.exists(_file_path):
            default_storage.mkdir(_file_path)

        _file_path = os.path.join(_file_path, name)

        url = settings.MEDIA_URL + '/'.join(path_receiver) + '/' + name
        return _file_path, url


