from django.apps import apps
get_model = apps.get_model
from celery.decorators import task
from haystack import connections

def remove_instance_from_index(instance):
    model_class = get_model(instance._meta.app_label, instance._meta.model_name)
    connection = connections['default']
    index = connection.get_unified_index().get_index(model_class)
    index.remove_object(instance)

@task(name="update_search_index")
def update_search_index(app_name, model_name, pk):
    model_class = get_model(app_name, model_name)
    instance = model_class.index_objects.get(pk=pk)
    connection = connections['default']
    index = connection.get_unified_index().get_index(model_class)
    index.update_object(instance)