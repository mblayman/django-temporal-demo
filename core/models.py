from django.contrib.auth.models import User
from django.db import models


class PoliticalParty(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"Political party ({self.name})"


class Escrow(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    receiving_party = models.OneToOneField(PoliticalParty, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0, help_text="Amount to store in cents")

    def __str__(self):
        return f"Escrow ({self.user.username})"
