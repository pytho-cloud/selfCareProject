from django.db import models

class Product(models.Model):
    product_purchase_date = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=255)
    product_price = models.IntegerField()

    def __str__(self):
        return self.product_name

class ProductExpense(models.Model):
    product_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_per_price = models.IntegerField()
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_total_purchase_price = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate the total purchase price before saving
        self.product_total_purchase_price = self.product_quantity * self.product_per_price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name
