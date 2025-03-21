from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    def __str__(self):
        return f"{self.item_name}"

    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://static.vecteezy.com/system/resources/previews/016/916/479/original/placeholder-icon-design-free-vector.jpg"
    )
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
