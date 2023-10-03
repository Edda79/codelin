# admin.py

from django.contrib import admin
from .models import Model3d

# Enregistrement du modèle Model3d dans l'interface d'administration
admin.site.register(Model3d)
