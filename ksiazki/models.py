from django.db import models


# Create your models here.

class ksiazki(models.Model):
    def __str__(self):
        return self.tytuł

    tytuł = models.CharField(max_length=200, null=True)
    autor = models.CharField(max_length=50, null=True)
    ISBN = models.CharField(max_length=40, null=True)
    data = models.DateField(None, null=True)
    strony = models.DecimalField(max_digits=4, decimal_places=0, null=True)
    jezyk = models.CharField(max_length=20, null=True)
    link = models.URLField(None, null=True)

    class Meta:
        verbose_name = "książka"
        verbose_name_plural = "książki"
