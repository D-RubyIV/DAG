from django.db import models


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