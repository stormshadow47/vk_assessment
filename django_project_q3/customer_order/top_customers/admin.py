# customer_order/admin.py

from django.contrib import admin
from top_customers.models import Customer, Order

# Inline class for entering orders under a customer
class OrderInline(admin.TabularInline):  # or use `StackedInline` for a different layout
    model = Order
    extra = 1  # Number of empty order forms to show by default

# Register the Customer model with Order inline
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    inlines = [OrderInline]  # Add the inline to the customer admin

# Optionally, you can also register the Order model on its own
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'status', 'total_amount')
    list_filter = ('status', 'order_date')
    search_fields = ('customer__name', 'status')
