# # 📖. Comment créer une application fullstack avec Django (backend) et React (frontend)

## Table des matières

A. [Backend: Django5](#1-backend-django5)  
    1. [Création d'un environnement virtuel](#1-création-dun-environnement-virtuel)  
    2. [Installation de Django5 et de Rest Framework](#2-installation-de-django5-et-de-rest-framework)  
    3. [Création du projet backend (sous-répertoire backend)](#3-création-du-projet-backend-sous-répertoire-backend)    
    4. [Création de l'application api](#4-création-de-lapplication-api)  
    5. [backend/backend/settings.py (paramètrage du projet)](#5-backendbackendsettingspy-paramètrage-du-projet)  
    6. [backend/backend/urls.py](#6-backendbackendurlspy)  
    7. [Création du fichier api/models.py](#7-création-du-fichier-apimodelspy)  
    8. [Démarrer l'application](#8-démarrer-lapplication)  
    9. [api/serializers.py](#9-apiserializerspy)  
    10. [backend/urls.py](#10-backendurlspy)  
    11. [api/views.py](#11-apiviewspy)  
    12. [api/urls.py](#12-apiurlspy)  
   <br>
B. [FrontEnd: React](#b-frontend-react)  
    1.[]  
    <br>
C. [Informations](#c-informations)  

---

## A. Backend: Django5
### 1. Création d'un environnement virtuel

```bash
mkdir /mnt/C/Fullstack-expense/backend
cd  /mnt/C/Fullstack-expense/backend
cd ..
source env/bin/activate
```

#### [Table des matières](#table-des-matières)

---

### 2. Installation de Django5 et de Rest Framework

```bash
pip install django djangorestframework
pip install django-cors-headers
```

#### [Table des matières](#table-des-matières)

---

### 3. Création du projet backend (sous-répertoire backend)

```bash
django-admin startproject backend .
```

> /mnt/c/Fullastack-expense/backend/backend

#### [Table des matières](#table-des-matières)

---

### 4. Création de l'application api

```bash
django-admin startapp api
```

#### [Table des matières](#table-des-matières)

---

### 5. backend/backend/settings.py (paramètrage du projet)

>Suppression des commentaires en en-tête

>Modification de la partie INSTALLED_APPS (voir api/apps.py/class ApiConfig(AppConfig) et rest_framework)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'rest_framework',
]
```

>Modification de la partie DATAASES

```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'transaction',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5437',
    }
}
```

#### [Table des matières](#table-des-matières)

---

### 6. backend/backend/urls.py

> Suppression des commentaires en en-tête

#### [Table des matières](#table-des-matières)

---

### 7. Création du fichier api/models.py 

```python
from django.db import models
import uuid

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.text} ({self.amount})"    
```

-#### [Table des matières](#table-des-matières)

---

```bash
python3 -m pip install djangorestframework
python3 -m pip install "psycopg[binary]"

/mnt/c/sources/fullstack-expense/backend$ python3 manage.py makemigrations
Migrations for 'api':
  api/migrations/0001_initial.p

python3 manage.py showmigrations
admin
 [ ] 0001_initial
 [ ] 0002_logentry_remove_auto_add
 [ ] 0003_logentry_add_action_flag_choices
api
 [ ] 0001_initial
auth
 [ ] 0001_initial
 [ ] 0002_alter_permission_name_max_length
 [ ] 0003_alter_user_email_max_length
 [ ] 0004_alter_user_username_opts
 [ ] 0005_alter_user_last_login_null
 [ ] 0006_require_contenttypes_0002
 [ ] 0007_alter_validators_add_error_messages
 [ ] 0008_alter_user_username_max_length
 [ ] 0009_alter_user_last_name_max_length
 [ ] 0010_alter_group_name_max_length
 [ ] 0011_update_proxy_permissions
 [ ] 0012_alter_user_first_name_max_length
contenttypes
 [ ] 0001_initial
 [ ] 0002_remove_content_type_name
sessions
 [ ] 0001_initial
```

#### [Table des matières](#table-des-matières)

---

>Aplliquer les migrations sur la base de données migration

```bash
ython3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, api, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying api.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

#### [Table des matières](#table-des-matières)

---

### 8. Démarrer l'application

```bash
/mnt/c/sources/fullstack-expense/backend$ python3 manage.py runserver

http://127.0.0.1:8000/ --> The install worked successfully! Congratulations!
```

#### [Table des matières](#table-des-matières)

---

### 9. api/serializers.py

>sérialisation: transformation d'un objet en texte

```python
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
```

#### [Table des matières](#table-des-matières)

---

### 10. backend/urls.py

```python
# Module d'administration de Django (interface /admin/)
from django.contrib import admin
# path : déclare une route ; include : délègue à un autre fichier d'URLs
from django.urls import path, include

# Liste des routes de niveau projet.
# Django la parcourt de haut en bas et utilise la première qui correspond.
urlpatterns = [
    # Toute URL commençant par "api/" est transmise au fichier api/urls.py.
    # Exemple : "api/transactions/" -> Django cherche "transactions/"
    # dans api/urls.py.
    path("api/", include('api.urls')),
]
```

#### [Table des matières](#table-des-matières)

---

### 11. api/views.py

```python
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
    # Ensemble d'objets sur lequel la vue travaille
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
```

#### [Table des matières](#table-des-matières)

---

### 12. api/test.rest

>Outil pour tester: REST Client. VSC > Ajouter Extension > REST Client

#### POST:Create, GET:Read, PUT:Update (Mettre à jour complètement une transaction), PATCH:Modification d'un seul champs

```rest
### ============================================================
### Tests de l'API des transactions (extension REST Client)
### Serveur : python3 manage.py runserver
### ============================================================

### 1. CRÉER une transaction
# POST sur la collection : le serveur génère l'id (UUID) et created_at.
# Copiez l'id renvoyé dans la réponse pour tester les requêtes suivantes.
POST http://localhost:8000/api/transactions/
Content-Type: application/json

{
  "text": "Salaire Juin",
  "amount": -2000.00
}

### 2. LISTER toutes les transactions
# GET sur la collection : renvoie un tableau JSON.
GET http://localhost:8000/api/transactions/

### 3. SUPPRIMER une transaction
# DELETE sur une transaction précise (UUID dans l'URL).
# Réponse attendue : 204 No Content. Un second appel donnera 404.
DELETE http://localhost:8000/api/transactions/7fe3245a-4b8d-4633-89cb-cea8715416c4/

### 4. MODIFIER une transaction (remplacement COMPLET)
# PUT exige tous les champs modifiables (text et amount),
# sinon DRF répond 400.
PUT http://localhost:8000/api/transactions/46e9110c-3590-473d-8492-2ffa6650ce36/
Content-Type: application/json

{
  "text": "Salaire février",
  "amount": 10000.00
}

### 5. MODIFIER une transaction (mise à jour PARTIELLE)
# PATCH n'envoie que les champs à changer (ici uniquement amount).
PATCH http://localhost:8000/api/transactions/46e9110c-3590-473d-8492-2ffa6650ce36/
Content-Type: application/json

{
  "amount": 60000.00
}
```

Cliquer sur Send Request pour voir les réultats.


---

**Fichier api/urls.py de test**

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.TransactionListCreateView.as_view())
]
```

python3 manage.py runserver

#### [Table des matières](#table-des-matières)

---

### 12. api/urls.py


```python
# Inutile ici : l'admin se déclare dans le urls.py principal du projet
from django.contrib import admin
# path : déclare une route
from django.urls import path
# Importe les vues définies dans api/views.py
from . import views

# Routes de l'application "api".
# Le préfixe "api/" est ajouté par le urls.py principal via include().
urlpatterns = [
    # /api/transactions/
    #   GET  -> liste des transactions
    #   POST -> création d'une transaction
    # as_view() convertit la classe de vue en fonction utilisable par Django
    path('transactions/', views.TransactionListCreateView.as_view()),

    # /api/transactions/<uuid>/ , par exemple :
    # /api/transactions/3fa85f64-5717-4562-b3fc-2c963f66afa6/
    #   GET          -> détail
    #   PUT / PATCH  -> modification
    #   DELETE       -> suppression
    # <uuid:id> capture un UUID et le passe à la vue sous le nom "id",
    # qui correspond au lookup_field = "id" de la vue.
    path('transactions/<uuid:id>/', views.TransactionRetrieveUpdateDestroyView.as_view()),
]
```

#### [Table des matières](#table-des-matières)

---

## B. FrontEnd: React
### 1. Installation de React

```bash
npx create-next-app@latest ./

Using npm.

Initializing project with template: app-tw


Installing dependencies:
- next
- react
- react-dom

Installing devDependencies:
- @tailwindcss/postcss
- @types/node
- @types/react
- @types/react-dom
- eslint
- eslint-config-next
- tailwindcss
- typescript
```

#### [Table des matières](#table-des-matières)

---

### 2. Vérification du fonctionnement de React

```bash
/mnt/c/Fullstack-expense/frontend$ npm run dev

Et cliquer sur : - Local: http://localhost:3000
```

#### [Table des matières](#table-des-matières)

---

### 3. frontend/app/page.tsx

```tsx
import Image from "next/image";

export default function Home() {
  return (
    <div>
      test
    </div>    
  );
}
```

```bash
/mnt/c/Fullstack-expense/frontend$ npm run dev
```

#### [Table des matières](#table-des-matières)

---

### 4. frontend/app/global.css

```css
@import "tailwindcss";
```

```bash
/mnt/c/Fullstack-expense/frontend$ npm run dev
```

#### [Table des matières](#table-des-matières)

---

### 5. Nettoygae des fichiers dans le répertoire public

- Suppression des fichiers: `file.svg`, `global.svg`, `next.svg`, `vercel.svg`, `window.svg`

#### [Table des matières](#table-des-matières)

---

### 6. saisyUI 

[Installez daisyUI en tant que plugin Tailwin](https://daisyui.com/docs/install/)

```bash
npm i -D daisyui@latest
```

#### [Table des matières](#table-des-matières)

---

### 7. Modifier le fichier global.css

```css
import Image from "next/image";

export default function Home() {
  return (
    <button className="btn btn-small">
      test
    </button>    
  );
}
;
```

#### [Table des matières](#table-des-matières)

---

### 8. Modifier le fichier page.tsx

```tsx
import Image from "next/image";

export default function Home() {
  return (
    <button className="btn btn-small">
      test
    </button>    
  );
}
```

```bash
/mnt/c/Fullstack-expense/frontend$ npm run dev
```

#### [Table des matières](#table-des-matières)

---

[Formation en cours](https://www.youtube.com/watch?v=gj8pTA3hNfM&t=3127s)

## C. Informations

[Tutoriel Django](https://www.geeksforgeeks.org/python/django-tutorial/)

#### [Table des matières](#table-des-matières)
