from django.db import models
from core.helpers import getUniqueId
from django.utils import timezone
from uuid import uuid4

# Create your models here.

class Insurance(models.Model):
    client = models.ForeignKey('accounts.ClientProfile', on_delete=models.CASCADE, related_name='client_insurance')
    ref_id = models.CharField('Reference ID', default=getUniqueId, max_length=10)
    insurance_type =  models.ForeignKey('insurance.InsuranceType', blank=True, null=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    amount = models.FloatField(default=10)
    employee = models.ForeignKey('accounts.EmployeeProfile', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta: 
        verbose_name = 'Insurance'
        verbose_name_plural = 'Insurances'
        ordering = ["-start_date", 'ref_id']
    
    def payMonth(self):
        return self.start_date.month
    
    # def duration(self):
    #     if self.end_date:
    #         import timedelta
    #         return self.end_date - (self.start_date.
    #     else:
    #         return "End Date not set"

    def __str__(self):
        return self.ref_id
    

class InsuranceType(models.Model):
    name = models.CharField(max_length=255)
    uui = models.UUIDField('Insurance Type Unique ID', default=uuid4,)
    summary = models.TextField()

    class Meta: 
        verbose_name = 'Insurance Type'
        verbose_name_plural = 'Insurance Types'
        ordering = ["-name",]

    def __str__(self):
        return self.name
    