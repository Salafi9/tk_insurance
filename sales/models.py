from django.db import models
from django.utils import timezone
from core.helpers import getUniqueId
from ckeditor.fields import RichTextField
# Create your models here.

class Transaction(models.Model):
    ref_id = models.CharField('Reference ID', default=getUniqueId, max_length=36)
    payment_date = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey('accounts.ClientProfile', on_delete=models.CASCADE, related_name='client_transactions')
    insurance = models.ForeignKey('insurance.Insurance', blank=True, null=True, on_delete=models.SET_NULL, related_name='transactions')
    amount = models.FloatField()
    summary = RichTextField(blank=True, null=True, help_text="Any Other Thought on the Transaction?")
    status = models.CharField(max_length=255, help_text="Completed, Half Pay or other Status")
    done = models.BooleanField(default=False, help_text="Mark of Succeful Transaction (Payment Recieved)")

    class Meta: 
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        ordering = ["-payment_date",]

    def pay_month(self):
        return self.payment_date.month

    def __str__(self):
        return self.ref_id