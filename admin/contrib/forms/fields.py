from django.db import models
from django.core.files.storage import get_storage_class


class S3PrivateFileField(models.FileField):
    """
    A FileField that gives the 'private' ACL to the files it uploads to S3, instead of the default ACL.
    """
    def __init__(self, verbose_name=None, name=None, upload_to='', storage=None, **kwargs):
        if storage is None:
            storage = get_storage_class()(acl='private',
                                          querystring_auth=True)
        super(S3PrivateFileField, self).__init__(verbose_name=verbose_name,
                                                 name=name,
                                                 upload_to=upload_to,
                                                 storage=storage,
                                                 **kwargs)
