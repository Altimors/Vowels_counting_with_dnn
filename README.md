# Comptage des voyelles d'une phrase en utilisant un réseau de neurones dense

A la suite de l'engouement général pour le machine learning ces dernières années, et pour concurrencer ChatGPT, j'ai décidé de vous présenter l'avenir de l'IA :

**Le calcul du nombre de voyelles d'une phrase par un réseau de neurones** (sans les accents parce que non)

## Utilisation 

### Besoins 

Pour exécuter, il vous faut au moins `Python 3.x` (pour ma part j'ai utilisé la version 3.10, je ne sais pas si ça marche avec les version antérieur mais j'imagine que oui)

Pour installer les dépendances : 

> pip install -r requirements.txt

ou 

> pip install tensorflow-cpu
 
> pip install numpy

Je vous conseille d'utiliser `tensorflow-cpu` pour éviter à avoir à gérer la configuration de la carte graphique. Surtout que le modèle n'est pas bien grand et les poids sont disponibles dans le fichier `model.h5`.

### Usage

Pour le lancer directement avec le modèle pré-entrainé, il suffit d'exécuter la commande suivante :

> python badcode.py "La phrase à analyser" -l

et pour l'entraîner :

> python badcode.py "La phrase à analyser"

Sachant que le fichier utilisé pour l'entraînement est `train.txt` et que le modèle sera sauvegardé à la fin. Par ailleurs, si vous voulez modifier les conditions d'entraînement, il faudra aller dans le code.