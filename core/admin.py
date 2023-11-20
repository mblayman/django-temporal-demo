from django.contrib import admin

from .models import Escrow, PoliticalParty


@admin.register(Escrow)
class Escrow(admin.ModelAdmin):
    pass


@admin.register(PoliticalParty)
class PoliticalParty(admin.ModelAdmin):
    pass
