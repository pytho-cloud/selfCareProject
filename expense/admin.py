from django.contrib import admin
from .models import Product, ProductExpense

# Register the Product model with custom display options
class ProductAdmin(admin.ModelAdmin):
    # List the fields you want to display in the admin list view as table columns
    list_display = ('product_name', 'product_price', 'product_purchase_date')

    # Optional: add filters or search options
    list_filter = ('product_price',)  # Filter by price for example
    search_fields = ('product_name',)  # Allow search by product name

admin.site.register(Product, ProductAdmin)


# Register the ProductExpense model with custom display options
class ProductExpenseAdmin(admin.ModelAdmin):
    # List the fields you want to display in the admin list view as table columns
    list_display = ('product_number', 'product_name', 'product_quantity', 'product_per_price', 'product_total_purchase_price')

    # Optional: add filters or search options
    list_filter = ('product_number', 'product_quantity')  # Filter by product_number or quantity for example
    search_fields = ('product_name',)  # Allow search by product name

    # Make 'product_total_purchase_price' readonly since it's calculated
    readonly_fields = ('product_total_purchase_price',)

admin.site.register(ProductExpense, ProductExpenseAdmin)
