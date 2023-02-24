from django.db import models
from cms_shared.models import PolicyType


class Policy(models.Model):
    type = models.ForeignKey(PolicyType, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)





