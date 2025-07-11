from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# id (primary key - automatico)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), picture (image)

# Depois 
# owner (foreign key)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' # desnecessario qdo plural for so o "s"

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts' # desnecessario qdo plural for so o "s"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    Category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    owner = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
