# -*- coding: utf-8 -*-
ERP_APPS = ['erp',]
DB_KEY = 'erp'


class ERPRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ERP_APPS:
            return DB_KEY
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ERP_APPS:
            return DB_KEY
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in ERP_APPS or obj2._meta.app_label in ERP_APPS:
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == DB_KEY:
            return model._meta.app_label in ERP_APPS
        elif model._meta.app_label in ERP_APPS:
            return False
        return None

