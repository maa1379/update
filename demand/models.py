from django.db import models
from account.models import User
from product.models import ProductBaseModel


# Create your models here.
class Hold(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hold")
    product = models.ForeignKey(ProductBaseModel, on_delete=models.CASCADE, related_name="hold")
    created = models.DateField(auto_now_add=True)
    description=models.TextField()



    def __str__(self):
        return f'{self.user} requested for holding {self.product}'
