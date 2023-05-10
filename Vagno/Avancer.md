# Rapport journalier de Vagnona

## To-do list 
- Lancer l'exercice 4 avec des lignes de commandes.
- Comprendre l'exercice 5 

## 19 avril 
- Comprendre et compliler le programme de l'exercice 4. 

J'ai pas encore compiler l'ex 4

## 23 avril 

    Ajout de Ex5_description.md

    Definitions des : scénarios, Métrique à évaluer, Configuration de l'ordonnancement.  

## 27 avril

Je lis la doc [suivante](https://docs.contiki-ng.org/en/develop/doc/programming/TSCH-and-6TiSCH.html)

1er jet possible : 
    Lancer plusieurs scénarios tous en comprenant comment scripter le truc. 
    Balancer des résultats brutes et Natha s'occupes de faire de joli graph + Rapport. 

Objectif d'aujourd'hui : Lancer et scripter le 1er scénarios.  

- Choses à faire mais c pas l'objectif d'aujourd'hui.
    - Penser à regarder les diff paramettre que l'on peut impliquer dans un profile pour les graph
    - Faire le tuto sniffer

J'ai lancé le scénario 0 mtn 
faire le scénario 0 avec une mesure de la communication radio et juste apres decale sur le scénario 1.
Pour ça faire le tuto profile Radio. 

## 29 avril 

Objectif :
- Faire le scénario 1 avec la conssomation d'energie
- Faire le scénario 0 avec la communication radio 

J'ai creé le script Conso d'energie du scénario 1 et 0 

Relancer le scénario1 energie mais 1 script = 1 nombre de noeud spécifique.
Faut faire la mesure de communication radio et faire des tests avec differentes couches MAC et commencer le rapport. 


## 7 mai 

- Check la conso d'energie 

- Se pencher un jour qur cette partie de code 

        /* 6TiSCH minimal schedule length.
        * Larger values result in less frequent active slots: reduces capacity and saves energy. */
        
        #define TSCH_SCHEDULE_CONF_DEFAULT_LENGTH 3

- Lecture de ce [site](https://docs.contiki-ng.org/en/develop/doc/tutorials/TSCH-and-6TiSCH.html) Pour capter 6TCSH et comprendre comment attraper la communication radio

- Les paramettres orchestra son dans orchestra.conf (Les paramettres son à modifier plus tard)

`Objectif pour la prochaine fois : `

- Faire des tests, sur la communication radio entre 2 noeuds simple parce que le profile TSCH_HOPPING_SEQUENCE_4_4 marche pas 
(Faire le tuto quoi)

- Puis Automatiser le tout pour voir la montée de charge 

- Tester d'autres scénarios

## 8 mai

Faut que la mesure de com radio fonctionne. 

## 9 mai 

    Mtn on spam des graph pour la RSSI et la conso d'energie. 
    On fait le sniffer demain
