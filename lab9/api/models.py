from django.db import models
from django.db.models import CharField, FloatField, TextField
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Company(models.Model):
    name = CharField(max_length=255)
    description = TextField()
    city = CharField(max_length=100)
    address = TextField()

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
        }

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = CharField(max_length=255)
    description = TextField()
    salary = FloatField()
    company = ForeignKey(Company, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company.name
        }

    def __str__(self):
        return self.name
