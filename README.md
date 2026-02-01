# Démonstration du Principe DRY (Don't Repeat Yourself) 🚀

Ce dépôt a pour but d'illustrer la différence fondamentale entre une approche WET (Write Everything Twice) et une approche DRY (Don't Repeat Yourself).



## 📝 Le Concept

L'objectif est de montrer comment l'automatisation et la centralisation des données permettent de créer un code plus solide et plus facile à maintenir. Comme je l'explique dans ma présentation, "plus une chose est grande, plus les responsabilités sont grandes" : coder moins permet d'avancer plus prudemment.



## 📁 Contenu du dépôt

version\_wet-dry.py : Une approche manuelle et répétitive (11 lignes de print). Ici, si la règle change, le programme risque de "devenir fou" car on doit tout modifier à la main ,et en suite  Une solution optimisée utilisant une fonction et une variable comme "source unique de vérité".



## 💡 Pourquoi passer au DRY ?

Gain de maintenance : On ne modifie la règle qu'à un seul endroit.



Lisibilité : On stocke la "formule mathématique" dans une fonction pour ne pas fatiguer le lecteur.



Fiabilité : On évite les oublis lors des mises à jour, ce qui garantit la cohérence pour l'utilisateur.

