# Exercice 5

## Objectif

Vous devez maintenant réaliser `une analyse de performance` du protocole `TSCH` et de l’ordonnancement `Orchestra`.

C’est à vous de définir les `scénarios` :  
- Modèles de trafic,
- Comparaison avec un autre protocole MAC,
- Etc...

les `métriques` que vous souhaitez évaluer :
  - PDR
  - Délai
  - Etc...

La configuration de `l’ordonnancement` :
- Règles, 
- Nombre de slotframes
- Taille,
- Etc.

La collection des résultats et leur mise en forme. 

*Vous attacherez la plus grande importance à la qualité de vos mesures : valeurs significatives, élimination des variations et des perturbations, etc.*

## un dépôt GIT sur git.unistra.fr sur lequel vous devrez déposer :

- les programmes utilisés pour réaliser les tests (fichiers C, Makefile, project-conf.h) ;
- les scripts et/ou programmes utilisés pour automatiser le lancement de vos expériences sur la plateforme FIT IOT-LAB;
- les fichiers résultats bruts (avant tout traitement) ;
- les scripts et/ou programmes utilisés pour générer les figures de résultat à partir des résultats bruts.
- Les sources du rapport et le rapport. 

## Dans le Rapport (à déposé en pdf sur moodle)

- une description de vos scénarios et leur justification
- la définition des métriques retenues, leur pertinence dans le contexte de cette étude, et comment vous les avez mesurées ;
- les résultats obtenus (sous la forme de graphiques) et la méthodologie pour leur génération;
- une analyse détaillée des résultats obtenus.

`10 pages max annexes comprises.`

# Note : 
la configuration utilisée par défaut dans Orchestra se trouve dans le fichier :  
    os/services/orchestra/orchestra-conf.h

Vous pouvez définir vos propres macros `ORCHESTRA_CONF_*` dans le fichier `project-conf.h` pour modifier cette configuration.
Vous trouverez également plus d’informations sur l’implémentation de TSCH [ici](https://github.com/contiki-ng/contiki-ng/wiki/Documentation:-TSCH-and-6TiSCH)