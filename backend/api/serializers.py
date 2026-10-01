# Importe le module des serializers de Django REST Framework (DRF)
from rest_framework import serializers
# Importe le modèle Transaction défini dans api/models.py
from .models import Transaction


# Un serializer convertit un objet Django (modèle) en JSON pour l'API,
# et inversement : il valide et transforme le JSON reçu en objet Python.
# ModelSerializer génère automatiquement les champs à partir du modèle.
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        # Le modèle sur lequel le serializer se base
        model = Transaction

        # Liste des champs exposés dans l'API (en lecture et en écriture)
        fields = ["id", "text", "amount", "created_at"]

        # Champs en lecture seule : renvoyés dans les réponses JSON,
        # mais ignorés si le client les envoie dans une requête POST/PUT.
        # "id" est généré par la base, "created_at" est rempli automatiquement.
        read_only_fields = ["id", "created_at"]