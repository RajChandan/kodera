from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class YearField(models.DateField):
    def __init__(self, *args, **kwargs):
        kwargs["validators"] = [
            MinValueValidator(2010),  # Specify the minimum year
            MaxValueValidator(2028),  # Specify the maximum year
        ]
        super().__init__(*args, **kwargs)


class Job(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class details(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    graduation_year = YearField()
    job_title = models.OneToOneField(Job, on_delete=models.CASCADE)
    contacted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
