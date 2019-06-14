from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Insurance, InsuranceType


class InsuranceResource(resources.ModelResource):
    class Meta:
        model = Insurance
        fields = ('client', 'ref_id', 'insurance_type', 'start_date', 'end_date', 'amount', 'employee')
        export_order = ('pk', 'client', 'ref_id', 'insurance_type', 'start_date', 'end_date', 'amount', 'employee')


class InsuranceAdmin(ImportExportModelAdmin):
    resource_class = InsuranceResource
    list_display = ['client', 'ref_id', 'insurance_type', 'start_date', 'end_date', 'amount', 'employee' ]
    search_fields = ['client', 'ref_id', 'start_date', 'employee']
    list_filter = ['insurance_type', 'start_date', 'end_date', 'employee'] 

# Register your models here.
admin.site.register(Insurance, InsuranceAdmin)
admin.site.register(InsuranceType)