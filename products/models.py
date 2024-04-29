from django.db import models
from django.conf import settings


class Products(models.Model):
    CATEGORY_CHOICES = (
        ("F", "Fruit"),
        ("V", "Vegetable"),
        ("M", "Meat"),
        ("O", "Other"),
    )

    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")

    def __str__(self):
        return self.title
