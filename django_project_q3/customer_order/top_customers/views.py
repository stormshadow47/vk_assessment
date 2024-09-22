from django.shortcuts import render
from top_customers.models import Order

def top_customers_view(request):
    top_customers = Order.top_customers_last_6_months()
    return render(request, 'top_customers.html', {'top_customers': top_customers})
