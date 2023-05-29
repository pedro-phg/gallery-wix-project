from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, URLValidator
from django.db import models
from .services.ValidationService import ValidationService

class Picture(models.Model):

    # def validation(self):
    #     ValidationService.validate_cpf(self.cpf)
    #     ValidationService.validate_phone_number(self.phone)
    #     ValidationService.validate_image_url(self.url)
    
    REGION_CHOICES = [
        ('Antártica', 'Antártica'),
        ('Ártico', 'Ártico'),
        ('Patagônia', 'Patagônia'),
    ]

    CATEGORY_CHOICES = [
        ('Paisagem', 'Paisagem'),
        ('Animal', 'Animal'),
        ('Ciência', 'Ciência'),
    ]


    fullName = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20, validators=[ValidationService.validate_cpf])
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator])
    phone = models.CharField(max_length=20, validators=[ValidationService.validate_phone_number])
    region = models.CharField(max_length=100, choices=REGION_CHOICES)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    url = models.URLField(validators=[ValidationService.validate_image_url])

    def __str__(self):
        return self.title