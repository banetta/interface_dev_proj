from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    p_id = models.PositiveBigIntegerField(db_column='p_Id', primary_key=True)  # Field name made lowercase.
    p_title = models.TextField()
    p_image = models.TextField()
    p_lprice = models.PositiveIntegerField()
    p_brand = models.CharField(max_length=45, blank=True, null=True)
    p_category1 = models.CharField(max_length=45, blank=True, null=True)
    p_category2 = models.CharField(max_length=45, blank=True, null=True)
    p_category3 = models.CharField(max_length=45, blank=True, null=True)
    p_category4 = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.p_title


class Review(models.Model):
    r_title = models.TextField()
    r_text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.r_title


class ShopBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    s_ordered = models.BooleanField(default=False)

    def __str__(self):
        return "[{}] {}".format(self.id, self.user.username)


class MyPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    m_emoney = models.PositiveIntegerField()

    def __str__(self):
        return "[{}] {}".format(self.id, self.user.username)
