
import threading
from .utils import hostname_from_request
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
THREAD_LOCAL = threading.local()


class DatabaseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        db = hostname_from_request(request).split('.')[0]
        setattr(THREAD_LOCAL, "DB", db)
        response = self.get_response(request)
        return response


class TenantMiddleware: 
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.session.get('tenant'):
            if request.path != reverse('company_selection') and request.path != reverse('admin:logout'):
                return HttpResponseRedirect(reverse_lazy('company_selection'))
        request.tenant=request.session.get('tenant')
        setattr(THREAD_LOCAL, "tenant", request.tenant)
        
        response = self.get_response(request)
        return response



def get_current_db_name():
    return getattr(THREAD_LOCAL, "DB", None)


def set_db_for_router(db):
    setattr(THREAD_LOCAL, "DB", db)