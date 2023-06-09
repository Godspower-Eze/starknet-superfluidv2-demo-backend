from django.db import models


class Pool(models.Model):
    account = models.CharField(max_length=250)
    token = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.address
