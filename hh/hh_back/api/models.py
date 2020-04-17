from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default=' ')
    city = models.CharField(max_length=100)
    address = models.TextField(default=' ')

    def __str__(self):
        return self.name + " " + self.city + " " + self.address

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class Vacancy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.name + " " + str(self.salary)

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"
