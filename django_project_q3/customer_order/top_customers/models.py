from django.db import models
from django.utils import timezone
from datetime import timedelta


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):
        return self.name



class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @staticmethod
    def top_customers_last_6_months(limit=5):
        six_months_ago = timezone.now() - timedelta(days=6*30)  
        from django.db.models import Sum
        top_customers = (Order.objects
                         .filter(order_date__gte=six_months_ago)
                         .values('customer__name')
                         .annotate(total_spent=Sum('total_amount'))
                         .order_by('-total_spent')[:limit])
        return top_customers
    