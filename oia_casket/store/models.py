from django.db import models

class Casket(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='caskets/')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    casket = models.ForeignKey(Casket, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
