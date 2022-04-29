from django.db import models
import uuid

# Create your models here.


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    category = models.CharField(max_length=300, verbose_name="Categoria")
    name = models.CharField(max_length=300, verbose_name="Transação")
    type = models.CharField(max_length=300, verbose_name="Tipo")
    value = models.FloatField(verbose_name="Valor")
    created_at = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = "Transação"
        verbose_name_plural = "Transações"

    def __str__(self):
        return self.name