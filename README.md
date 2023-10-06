# UK-WildlifeTracker-DockerEdition

# Projet Mammals

Ce projet est une application Web qui permet de visualiser et d'explorer des données sur les mammifères. Il utilise FastAPI pour l'API backend et Streamlit pour l'interface utilisateur frontend.

## Configuration préalable

#Avant de commencer, assurez-vous d'avoir effectué les étapes suivantes :

##1. Clonez ce référentiel sur votre machine locale :

```bash
git clone https://github.com/VotreNomDeCompteGitHub/projet-mammals.git


#Accédez au répertoire du projet :

##  cd projet-mammals


Décompressez le fichier de données Mammals.zip qui se trouve dans le dossier mongo_seed. Vous pouvez utiliser un utilitaire de décompression de fichiers comme unzip.
Lancement de l'application
Pour exécuter l'application, suivez les étapes ci-dessous :

Assurez-vous que Docker est installé sur votre machine.

Ouvrez un terminal et exécutez la commande suivante pour lancer la conteneurisation :

## docker-compose up --build -d

Attendez que les conteneurs se construisent et se lancent. Une fois terminé, les services FastAPI et Streamlit devraient être accessibles.

#Accédez à l'application Streamlit en ouvrant un navigateur Web et en visitant l'URL suivante :


## http://localhost:8002/


Vous pouvez maintenant explorer et visualiser les données sur les mammifères à l'aide de l'interface Streamlit.
Arrêt de l'application
#Pour arrêter l'application, vous pouvez exécuter la commande suivante dans le répertoire du projet :

## docker-compose down


Cela arrêtera les conteneurs Docker en cours d'exécution.

Remarques
Les données initiales sont fournies sous forme de fichier Mammals.zip dans le dossier mongo_seed. Assurez-vous de décompresser ce fichier pour accéder au jeu de données.

Vous pouvez personnaliser davantage l'application et ajouter des fonctionnalités supplémentaires selon vos besoins.

Si vous rencontrez des problèmes ou avez des questions, n'hésitez pas à créer une issue dans ce référentiel.

Profitez de l'exploration des données sur les mammifères !
