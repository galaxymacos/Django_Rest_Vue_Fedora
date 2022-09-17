from django.contrib import admin

from artifacts.models import Artifact


# Register your models here.
@admin.register(Artifact)
class ArtifactAdmin(admin.ModelAdmin):
    list_display = ("name", "shiny")
