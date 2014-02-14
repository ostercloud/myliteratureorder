from django.db import models

# Create your models here.


class SpecialOrder(models.Model):
    item = models.CharField(max_length=200)
    ordered_by = models.CharField(max_length=200)
    order_date = models.DateField('Date Ordered')
    received_date = models.DateField('Date Received', null=True, blank=True)
    fulfilled_date = models.DateField('Date Fulfilled', null=True, blank=True)
    quantity = models.IntegerField('Quantity Ordered')

    def __unicode__(self):
        return unicode(self.item)

    class Meta:
        verbose_name = u"SpecialOrder"
        verbose_name_plural = verbose_name


class BulkOrder(models.Model):
    item = models.CharField(max_length=200)
    ordered_by = models.CharField(max_length=200)
    order_date = models.DateField('Date Ordered')
    received_date = models.DateField('Date Received', null=True, blank=True)
    fulfilled_date = models.DateField('Date Fulfilled', null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.item)

    class Meta:
        verbose_name = u"BulkOrder"
        verbose_name_plural = verbose_name