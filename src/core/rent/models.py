from django.db import models

# Create your models here.

class Rent(models.Model):
    """Respents a "user profile" inside our system."""

    user = models.ForeignKey('authentication.UserProfile', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    transactionDate = models.DateTimeField(auto_now_add=True, blank=True)


