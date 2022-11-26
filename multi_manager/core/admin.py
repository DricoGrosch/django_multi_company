from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import *
admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Product)

@admin.register(User)
class UserAdmin(UserAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return self.model.admin_objects.all()
        return super().get_queryset(request)
