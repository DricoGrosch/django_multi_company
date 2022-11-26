from django.db import models
from .middleware import THREAD_LOCAL
from django.contrib.auth.models import UserManager
class TenantManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        if getattr(THREAD_LOCAL,'tenant',None):
            qs = qs.filter(company=THREAD_LOCAL.tenant)
        return qs

class TenantUserManager(UserManager):
    def get_queryset(self):
        qs = super().get_queryset()
        if getattr(THREAD_LOCAL,'tenant',None):
            qs = qs.filter(companies=THREAD_LOCAL.tenant) | qs.filter(companies__isnull=True)
        return qs