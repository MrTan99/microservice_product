from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Product(models.Model):
  name = models.CharField(max_length=100, blank=False)
  description = models.CharField(max_length=150, blank=False)
  price = models.DecimalField(max_digits=20, blank=False, null=False, decimal_places=2)
  stock = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(100)], blank=False)
  date = models.DateTimeField(auto_now_add=True, blank=True)
  product_picture = models.ImageField(null=True, blank=True, upload_to="images/")
  status = models.CharField(max_length=20, blank=False)
      
  def __str__(self):
    return self.name