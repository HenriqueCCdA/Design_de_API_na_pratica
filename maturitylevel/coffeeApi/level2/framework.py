from datetime import datetime
import functools
from http import HTTPStatus
import json


from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.test import Client
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

from coffeeApi.level2.domain import DoesNotExist


DEFAULT_CT = 'application/json'

class MyResponse(HttpResponse):
    def __init__(self, *args, **kwargs):
        headers = kwargs.setdefault('headers', {})

        if 'Content-Type' not in headers:
            headers['Content-Type'] = DEFAULT_CT

        super().__init__(*args, **kwargs)


class MethodNotAllewed(MyResponse):
    status_code = HTTPStatus.METHOD_NOT_ALLOWED

    def __init__(self, *args, **kwargs):
        super().__init__(
            HTTPStatus.METHOD_NOT_ALLOWED.description,
            *args, **kwargs
        )


class BadRequest(MyResponse):
    status_code = HTTPStatus.BAD_REQUEST


class Created(MyResponse):
    status_code = HTTPStatus.CREATED


class NotFound(MyResponse):
    status_code = HTTPStatus.NOT_FOUND


class NoContent(MyResponse):
    status_code = HTTPStatus.NO_CONTENT


class Ok(MyResponse):
    status_code = HTTPStatus.OK


class allow:

    def __init__(self, methods):
        self.allowed = tuple(m.upper() for m in methods)

    def __call__(self, view):
        @functools.wraps(view)
        def wrapper(request, *args, **kwargs):
            if request.method not in self.allowed:
                return MethodNotAllewed()

            return view(request, *args, **kwargs)

        return wrapper


class require:

    def __init__(self, *params):
        self.params = params

    def __call__(self, view):
        @functools.wraps(view)
        def wrapper(request, *args, **kwargs):
            try:
                params = {k: request.GET[k] for k in self.params}
            except MultiValueDictKeyError as e:
                return BadRequest(str(e).strip("'"))
            kwargs['params'] = params
            return view(request, *args, **kwargs)

        return wrapper


class data_required:

    def __init__(self, *params):
        self.params = params

    def __call__(self, view):
        @functools.wraps(view)
        def wrapper(request, *args, **kwargs):
            try:
                params = json.loads(request.body)
                assert all(p in params for p in self.params)
            except AssertionError as e:
                return BadRequest('Bad request.')
            kwargs['params'] = params
            return view(request, *args, **kwargs)

        return wrapper


class FrameworkCommonExceptionHandler:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exc):
        if isinstance(exc, DoesNotExist):
            return NotFound()


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

def abs_reverse(request, viewname, args=None, kwargs=None, current_app=None):
    return  request.build_absolute_uri(
        reverse(viewname, args=args, kwargs=kwargs, current_app=current_app)
    )


def serialize(obj):
    return json.dumps(vars(obj), cls=MyJSONEncoder)


def deserialize(s):
    return json.loads(s, cls=MyJSONEDecoder)


class MyJSONEncoder(DjangoJSONEncoder):
    pass


class MyJSONEDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.hook, *args, **kwargs)

    @staticmethod
    def hook(source):
        d ={}
        for k, v in source.items():
            if isinstance(v, str) and not v.isdigit():
                try:
                    d[k] = datetime.fromisoformat(v)
                except (ValueError, TypeError):
                    d[k] = v

            else:
                d[k] = v
        return d