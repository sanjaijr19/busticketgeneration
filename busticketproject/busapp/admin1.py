from  django.contrib import admin

from .models import Driver

@admin.register(Driver)
class Driveradmin1(admin.ModelAdmin):
    list_display = ("name",)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form=super().get_form(request,obj,**kwargs)
        is_superuser=request.user.is_superuser


        if not is_superuser:
            form.base_fields['name'].disabled=True
        return form
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return False