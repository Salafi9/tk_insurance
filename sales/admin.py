from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Transaction

class TransactionResource(resources.ModelResource):
    class Meta:
        model = Transaction
        fields = ('client', 'ref_id', 'insurance_type', 'payment_date', 'amount', 'status', 'done')
        export_order = ('pk', 'client', 'ref_id', 'insurance_type', 'payment_date', 'amount', 'status', 'done')


class TransactionAdmin(ImportExportModelAdmin):
    resource_class = TransactionResource
    list_display = [ 'ref_id', 'client', 'insurance', 'amount', 'done', ]
    search_fields = ['client', 'ref_id', 'payment_date', 'summary']
    list_filter = ['done', 'payment_date', 'insurance',] 

# Register your models here.
admin.site.register(Transaction, TransactionAdmin)