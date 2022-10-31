# <img title="Jardi'Quest logo" alt="Logo de jardi'quest" src="./.res-readme/Jardi'Quest.svg" style="height: 65px; width: 65px; vertical-align: middle" width="65" height="65" >PPII «Projet Pluridisciplinaire d'Informatique Intégrative» (2022-2023) 

Olivier Festor <<olivier.festor@telecomnancy.eu>>  
Anne-Claure Heurtel <<anne-claire.heurtel@telecomnancy.eu>>  
Gérald Oster <<gerald.oster@telecomnancy.eu>>  


## Jardi'Quest

**Membres du groupe** :
- ARIES Lucas <<Lucas.Aries@telecomnancy.eu>>  
- DEVAUX Paul <<Paul.Deveaux@telecomnancy.eu>>  
- HORNBERGER Théo <<Theo.Hornberger@telecomnancy.eu>>  
- TEMPESTINI Terry <<Terry.Tempestini@telecomnancy.eu>>  

## Description du projet

<img title="Jardi'Quest logo" alt="Logo de jardi'quest" src="./.res-readme/Jardi'Quest.svg" style="height: 200px; width: 200px; margin: auto; display: block" width="200" height="200">

**Application Web** qui permet de gérer un **jardin** de façon **innovante** a l'aide de **quête**.
Plus besoin de séparer son jardin en parcelle, ici tout le monde travaille main dans la main pour être récompensé et recevoir les fruits de son labeur.


## Installation du projet
Au root du projet veuillez effectuer ses commandes pour installer et lancer l'application
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run --host=0.0.0.0 --port=5454
```

## Lancement du projet
Après avoir installé le projet vous pouvez le lancer en étant au root du projet avec
```bash
source venv/bin/activate
flask run
```

## Lancement des tests
Dans le root du projet effectué :
```bash
source venv/bin/activate
pytest
```