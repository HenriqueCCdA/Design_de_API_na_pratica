import functools
from django.test import Client


from .http import DEFAULT_CT

# class APIClient(Client):
#     def post(self, *args, **kwargs):
#         kwargs['content_type'] = DEFAULT_CT
#         return super().post(*args, **kwargs)

#     def get(self, *args, **kwargs):
#         kwargs['content_type'] = DEFAULT_CT
#         return super().get(*args, **kwargs)

#     def put(self, *args, **kwargs):
#         kwargs['content_type'] = DEFAULT_CT
#         return super().put(*args, **kwargs)

#     def delete(self, *args, **kwargs):
#         kwargs['content_type'] = DEFAULT_CT
#         return super().delete(*args, **kwargs)

APIClient = type('APIClient',
                 (Client,),
                 {verb: functools.partialmethod(getattr(Client, verb), content_type=DEFAULT_CT)
                 for verb in ('post', 'get', 'put', 'delete')})