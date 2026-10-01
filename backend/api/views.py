# render sert à renvoyer des pages HTML : inutile ici, une API renvoie du JSON
from django.shortcuts import render
# Vues génériques de DRF : elles contiennent déjà toute la logique CRUD
from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer


# Vue pour la collection de transactions :
#   GET  -> renvoie la liste de toutes les transactions
#   POST -> crée une nouvelle transaction
class TransactionListCreateView(generics.ListCreateAPIView):
    # Ensemble d'objets Transaction sur lequel la vue travaille
    queryset = Transaction.objects.all()
    # Serializer utilisé pour valider les données reçues
    # et convertir les objets en JSON
    serializer_class = TransactionSerializer


# Vue pour UNE transaction précise :
#   GET          -> détail
#   PUT / PATCH  -> modification (complète / partielle)
#   DELETE       -> suppression
class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # Champ utilisé pour retrouver l'objet dans l'URL.
    # Par défaut DRF utilise "pk" ; ici on demande "id",
    # donc l'URL devra contenir <int:id> et non <int:pk>.
    lookup_field = "id"
